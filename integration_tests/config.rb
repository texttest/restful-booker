# Full path to the System Under Test (or Java Main Class name)
executable:${TEXTTEST_ROOT}/test_rig.py

home_operating_system:nt
interpreter:${TEXTTEST_ROOT}/venv/Scripts/python.exe

# Naming scheme to use for files for stdin,stdout and stderr
filename_convention_scheme:standard

# Expanded name to use for application
full_name:Restful Booker

dbtext_database_path:mongodata

import_config_file:capturemock_config

copy_test_path:${TEXTTEST_ROOT}/../oas.yaml

[run_dependent_text]
stdout:(url http://)(127.0.0.1|localhost):\d+{REPLACE \1<localhost_port>}
httpmocks:"token":"[\d\w]+"{REPLACE "token": "atoken"}
stderr:restful-booker-v2:server Listening on port
