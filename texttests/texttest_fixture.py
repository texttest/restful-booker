#!/usr/bin/env python3

import os, sys, time, io
import requests, json
from subprocess import Popen, PIPE

def is_json(response):
    return "json" in response.headers["Content-Type"]


def read_key_value_file(headers_filename):
    headers = {}
    if os.path.exists(headers_filename):
        with open(headers_filename, encoding="utf-8") as f:
            for line in f:
                key, value = line.split(":")
                headers[key.strip()] = value.strip()
    return headers


def write_key_value(the_dict, filename):
    if not the_dict:
        return
    with open(filename, "w") as f:
        for header, value in sorted(the_dict.items()):
            f.write(f"{header}: {value}\n")

def do_post(full_url, headers, cookies):
    if not os.path.exists("request_body.json"):
        sys.stderr.write("could not find request body for post")
        sys.exit(1)
    with io.open("request_body.json", "r", encoding="utf-8") as f:
        payload = json.loads(f.read())
        r = requests.post(full_url, json=payload, headers=headers, cookies=cookies)
        return r

def do_request_response():
    if not os.path.exists("rest_command.txt"):
        sys.stderr.write("could not find rest command, exiting\n")
        sys.exit(1)

    with open("rest_command.txt", "r", encoding="utf-8") as f:
        rest, url = f.read().split()
        sys.stdout.write(f"found rest command {rest} for url {url}\n")

    BASE_URL = "http://localhost:3001"
    if len(sys.argv) > 1:
        BASE_URL = sys.argv[1]
    full_url = f"{BASE_URL}{url}"

    headers = read_key_value_file("request_headers.txt")
    cookies = read_key_value_file("request_cookies.txt")

    if "GET" in rest.upper():
        r = requests.get(full_url, headers=headers, cookies=cookies)
    if "POST" in rest.upper():
        r = do_post(full_url, headers, cookies)

    with open("status_code.txt", "w") as f:
        f.write(str(r.status_code))

    if is_json(r):
        with open("response.json", "w") as f:
            f.write(r.text)
    else:
        with open("response.txt", "w") as f:
            f.write(r.text)

    write_key_value(r.headers, "response_headers.txt")
    write_key_value(r.cookies, "response_cookies.txt")

def start_server():
    print("starting server")
    texttest_home = os.environ["TEXTTEST_HOME"]
    cwd = os.getcwd()
    os.environ["LOAD_DB"] = "true"
    os.environ["DB_FILE"] = os.path.join(cwd, "db.json")
    p = Popen([f"{texttest_home}/bin/www"],
           shell=True,
           cwd=os.getcwd(), stdout=PIPE)
    count = 0
    while count < 3:
        msg = p.stdout.readline()
        if b"db loaded" in msg:
            time.sleep(0.05)
            break
        else:
            print(msg)
        count += 1
    return p

def stop_server(process):
    print("stopping server")
    process.terminate()

if __name__ == "__main__":
    process = start_server()
    try:
        do_request_response()
    finally:
        stop_server(process)