#!/usr/bin/env python3

import os, sys, json
import requests


class NullResponse:
	pass
BASE_URL = "http://localhost:3001"


def is_json(response):
	try:
		json.loads(response.text)
		return True
	except (json.JSONDecodeError, TypeError) as e:
		return False


if __name__ == "__main__":
	if not os.path.exists("rest_command.txt"):
		sys.stderr.write("could not find rest command, exiting\n")
		sys.exit(1)

	with open("rest_command.txt", "r") as f:
		rest, url = f.read().split()
		sys.stdout.write(f"found rest command {rest} for url {url}\n")

	r = NullResponse()
	r.status_code = "No response"
	r.text = "No response"

	if "GET" in rest.upper():
		sys.stdout.write("get request")
		r = requests.get(f"{BASE_URL}{url}")
	if "POST" in rest.upper():
		if not os.path.exists("payload.json"):
			sys.stderr.write("could not find payload for post")
			sys.exit(1)
		with open("payload.json") as f:
			payload = f.read()
			sys.stdout.write(f"will post payload\n")
			r = requests.post(f"{BASE_URL}{url}", data=payload)

	with open("status_code.txt", "w") as f:
		f.write(str(r.status_code))
	if is_json(r):
		with open("response.json", "w") as f:
			f.write(r.text)
	else:
		with open("response.txt", "w") as f:
			f.write(r.text)
			