#!/usr/bin/env python3

import os, sys
import requests, json


class NullResponse:
	pass


def is_json(response):
	return "json" in response.headers["Content-Type"]


if __name__ == "__main__":
	if not os.path.exists("rest_command.txt"):
		sys.stderr.write("could not find rest command, exiting\n")
		sys.exit(1)

	with open("rest_command.txt", "r") as f:
		rest, url = f.read().split()
		sys.stdout.write(f"found rest command {rest} for url {url}\n")

	BASE_URL = "http://localhost:3001"
	if len(sys.argv) > 1:
		BASE_URL = sys.argv[1]

	headers = {}
	if os.path.exists("headers.txt"):
		with open("headers.txt") as f:
			for line in headers:
				key, value = line.split()
				headers[key] = value

	r = NullResponse()
	r.status_code = "No response"
	r.text = "No response"

	if "GET" in rest.upper():
		sys.stdout.write("get request")
		r = requests.get(f"{BASE_URL}{url}", headers=headers)
	if "POST" in rest.upper():
		if not os.path.exists("payload.json"):
			sys.stderr.write("could not find payload for post")
			sys.exit(1)
		with open("payload.json") as f:
			payload = f.read()
			sys.stdout.write(f"will post payload\n")
			r = requests.post(f"{BASE_URL}{url}", data=payload, headers=headers)

	with open("status_code.txt", "w") as f:
		f.write(str(r.status_code))
	if is_json(r):
		with open("response.json", "w") as f:
			response_json = json.loads(r.text)
			f.write(r.text)
	else:
		with open("response.txt", "w") as f:
			f.write(r.text)

	with open("headers.txt", "w") as f:
		for header, value in sorted(r.headers.items()):
			f.write(f"{header}: {value}\n")

	if r.cookies:
		with open("cookies.txt", "w") as f:
			f.write(str(r.cookies))