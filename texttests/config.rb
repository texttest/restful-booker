# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_HOME}/texttests/texttest_fixture.py
interpreter:python3

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:Restful Booker

link_test_path:rest_command.txt
link_test_path:request_body.json
link_test_path:request_headers.txt
link_test_path:request_cookies.txt
copy_test_path:db.json

[collate_file]
status_code:status_code.txt
response_json:response.json
response_text:response.txt
response_cookies:response_cookies.txt
response_headers:response_headers.txt
final_db:db.json


[collate_script]
response_json:python3 -m json.tool
final_db:python3 -m json.tool

[run_dependent_text]
response_headers:Date
response_headers:ETag
#response_json:"token": "[\d\w]+"{REPLACE "token": "atoken"}
stderr:restful-booker-v2:server Listening on port