# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_ROOT}/test_rig.py

home_operating_system:nt
interpreter:${TEXTTEST_ROOT}/venv/Scripts/python.exe

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:Restful Booker

copy_test_path:mongodata
copy_test_path:capturemock.rc

# Configuration for integration with "CaptureMock"
[definition_file_stems]
regenerate:httpmocks

[run_dependent_text]
stdout:(url http://localhost:)\d+{REPLACE \1<port>}
httpmocks:"token":"[\d\w]+"{REPLACE "token": "atoken"}
stderr:restful-booker-v2:server Listening on port
