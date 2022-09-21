#!/usr/bin/env python

import logging
import os
import sys

from http_text_cli import do_request_response, get_base_url
from http_text_cli import start_server, stop_server, find_unique_port
import dbtext

if __name__ == "__main__":
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.getLogger().setLevel(logging.INFO)

    testdbname = "ttdb_" + str(os.getpid()) # some temporary name not to clash with other tests
    with dbtext.LocalMongo_DBText(testdbname, transactions=False) as db: # the name you use here will be used for the directory name in the current working directory
        if not db.setup_succeeded(): # could not start MongoDB, for example
            sys.exit(1)

        testConnStr = "mongodb://localhost:" + str(db.port) # provide to your system in some way
        port = find_unique_port()
        url = get_base_url(host="localhost", port=port)
    
        my_env = dict()
        my_env["BOOKER_DB_URL"] = testConnStr
        
        texttest_home = os.path.dirname(os.environ.get("TEXTTEST_ROOT"))
    
        logging.info(f"starting Restful Booker on url {url}")
    
        process = start_server(
            command=["node", f"{texttest_home}/bin/www"],
            port=port,
            additional_environment=my_env,
        )
        try:
            do_request_response(base_url=url)
        finally:
            stop_server(process)
        
        db.dump_changes("rb") # dump changes in all the tables you're interested in. "myext" is whatever extension you want to use, probably the TextTest one 
