#!/usr/bin/env python

import logging, os, sys, socket, time
from subprocess import Popen, PIPE
import capturemock
import dbtext

def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        return s.getsockname()[1]

if __name__ == "__main__":
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.getLogger().setLevel(logging.INFO)

    testdbname = "ttdb_" + str(os.getpid()) # some temporary name not to clash with other tests
    with dbtext.LocalMongo_DBText(testdbname, transactions=False) as db:
        if not db.setup_succeeded(): # could not start MongoDB, for example
            sys.exit(1)

        testConnStr = "mongodb://localhost:" + str(db.port)
        port = find_available_port()
        url = f"http://localhost:{port}"
        
        my_env = os.environ.copy()
        my_env["BOOKER_DB_URL"] = testConnStr
        my_env["PORT"] = str(port)
        
        texttest_home = os.path.dirname(os.environ.get("TEXTTEST_ROOT"))
        command=["node", f"{texttest_home}/bin/www"]
    
        logging.info(f"starting Restful Booker on url {url}")
    
        process = Popen(command, stdout=PIPE, env=my_env)
        try:
            capturemock.replay_for_server(serverAddress=url)
        finally:
            logging.info("stopping Restful Booker")
            process.terminate()
        
        db.dump_changes("rb")