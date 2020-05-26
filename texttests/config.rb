# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_HOME}/texttests/texttest_fixture.py
interpreter:python3

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:Restful Booker

link_test_path:rest_command.txt
link_test_path:payload.json

[collate_file]
status_code:status_code.txt
response_json:response.json
response_text:response.txt
response_cookies:cookies.txt


[collate_script]
response_json:python3 -m json.tool
