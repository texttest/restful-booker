#!/usr/bin/env python

import logging, os, sys, socket, webbrowser, time
from subprocess import Popen
import capturemock
import dbtext

def find_available_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        return s.getsockname()[1]
    
def wait_for_file(fn):
    for _ in range(600):
        if os.path.isfile(fn) and os.path.getsize(fn) > 0:
            time.sleep(1) # allow time for flush
            return
        else:
            time.sleep(0.1)
    print("Timed out waiting for action after 1 minute!", file=sys.stderr)

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
        
        replayFile, recordFile = capturemock.get_default_setup_for_texttest()
        record = replayFile is None
        if record:
            recordFile = "httpmocks.rb"
            capturemock.setUpServer(capturemock.RECORD, recordFile, rcFiles=["capturemock.rc"], 
                                    environment=my_env, recordFromUrl=url)
        
        texttest_home = os.path.dirname(os.environ.get("TEXTTEST_ROOT"))
        command=["node", f"{texttest_home}/bin/www"]
    
        logging.info(f"starting Restful Booker on url {url}")
    
        process = Popen(command, stdout=open("restful-booker.txt", "w"), env=my_env)
        try:
            if record:
                webbrowser.open_new(url + "/api-docs")
                wait_for_file(recordFile)
            else:
                capturemock.replay_for_server("capturemock.rc", replayFile, recordFile, url)
        finally:
            logging.info("stopping Restful Booker")
            process.terminate()
            capturemock.terminate()
        
        db.dump_changes("rb")