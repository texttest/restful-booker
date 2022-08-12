#!/usr/bin/env python

import logging
import os
import sys

import requests
from http_text_cli import do_request_response, get_base_url
from http_text_cli import start_server, stop_server, find_unique_port

if __name__ == "__main__":
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.getLogger().setLevel(logging.INFO)

    port = find_unique_port()
    url = get_base_url(host="localhost", port=port)

    cwd = os.getcwd()
    my_env = dict()
    my_env["LOAD_DB"] = "true"
    my_env["DB_FILE"] = os.path.join(cwd, "db.json")

    texttest_home = os.environ.get("TEXTTEST_HOME", cwd)

    logging.info(f"starting Restful Booker on url {url}")

    process = start_server(
        command=["node", f"{texttest_home}/bin/www"],
        port=port,
        additional_environment=my_env,
    )
    try:
        do_request_response(base_url=url)

        if "--dumpdb" in sys.argv:
            r = requests.get(url + "/dumpdb", headers={"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="})
            logging.info(f"requested to dump db, got response {r.status_code}")

    finally:
        stop_server(process)
