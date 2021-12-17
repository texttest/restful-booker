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

def get_payload():
    if not os.path.exists("request_body.json"):
        sys.stderr.write("could not find request body")
        sys.exit(1)
    with io.open("request_body.json", "r", encoding="utf-8") as f:
        payload = json.loads(f.read())
        return payload

def do_post(full_url, headers, cookies):
    payload = get_payload()
    return requests.post(full_url, json=payload, headers=headers, cookies=cookies)

def do_put(full_url, headers, cookies):
    payload = get_payload()
    return requests.put(full_url, json=payload, headers=headers, cookies=cookies)

def do_patch(full_url, headers, cookies):
    payload = get_payload()
    return requests.patch(full_url, json=payload, headers=headers, cookies=cookies)

def do_delete(full_url, headers, cookies):
    return requests.delete(full_url,headers=headers, cookies=cookies)

def do_request_response(port=3001):
    if not os.path.exists("rest_command.txt"):
        sys.stderr.write("could not find rest command, exiting\n")
        sys.exit(1)

    with open("rest_command.txt", "r", encoding="utf-8") as f:
        rest, url = f.read().split()
        sys.stdout.write(f"found rest command {rest} for url {url}\n")

    BASE_URL = f"http://localhost:{port}"
    full_url = f"{BASE_URL}{url}"

    headers = read_key_value_file("request_headers.txt")
    cookies = read_key_value_file("request_cookies.txt")

    if "GET" in rest.upper():
        r = requests.get(full_url, headers=headers, cookies=cookies)
    elif "POST" in rest.upper():
        r = do_post(full_url, headers, cookies)
    elif "PUT" in rest.upper():
        r = do_put(full_url, headers, cookies)
    elif "PATCH" in rest.upper():
        r = do_patch(full_url, headers, cookies)
    elif "DELETE" in rest.upper():
        r = do_delete(full_url, headers, cookies)

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
    if "--dumpdb" in sys.argv:
        r = requests.get(BASE_URL + "/dumpdb", headers={"Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="})
        print(f"requested to dump db, got response {r.status_code}")


def find_unique_port(minimum_port=3001):
    """Returns a port that is:
        - greater than or equal to the minimum_port given
        - unique for the currently executing test case (to avoid test collisions)
    """
    unique_string = os.environ.get("TEXTTEST_SANDBOX")
    if unique_string is None:
        return str(minimum_port)
    port = abs(hash(unique_string)) % (65536 - minimum_port)
    port += minimum_port
    return f"{port}"

def start_server(port):
    print("starting server")
    cwd = os.getcwd()
    texttest_home = os.environ.get("TEXTTEST_HOME", cwd)
    my_env = os.environ.copy()
    my_env["LOAD_DB"] = "true"
    my_env["DB_FILE"] = os.path.join(cwd, "db.json")
    my_env["PORT"] = port

    p = Popen([f"{texttest_home}/bin/www"],
           shell=True,
           cwd=cwd,
           stdout=PIPE,
           env=my_env)
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
    port = find_unique_port()
    process = start_server(port)
    try:
        do_request_response(port=port)
    finally:
        stop_server(process)