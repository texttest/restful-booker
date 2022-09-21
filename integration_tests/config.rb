# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_ROOT}/test_rig.py

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:Restful Booker

link_test_path:request_url.txt
link_test_path:request_body.json
link_test_path:request_headers.txt
link_test_path:request_cookies.txt
copy_test_path:mongodata

#create_catalogues:true

[collate_file]
status_code:response_status_code.txt
response_json:response_body.json
response_text:response_body.txt
response_cookies:response_cookies.txt
response_headers:response_headers.txt

[collate_script]
response_json:python -m json.tool

[run_dependent_text]
stdout:(url http://localhost:)\d+{REPLACE \1<port>}
response_headers:Date
response_headers:ETag
response_json:"token": "[\d\w]+"{REPLACE "token": "atoken"}
stderr:restful-booker-v2:server Listening on port
final_db:"_id": "[\d\w]+"{REPLACE "_id": "id"}