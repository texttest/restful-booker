# restful-booker
A simple Node booking form for testing RESTful web services.

## Installation
In order to run restful booker you will need to install:
1. npm and node
2. mongo db

From this folder you should then be able to execute:

    npm install
    npm start

Restful booker should then start running on [localhos](https://localhost:3001/) and you can access it from a browser.

## Integration tests with TextTest

In order to run the [TextTest](https://texttest.org) integration tests in the folder 'integration_tests'
you will need to install:

1. Python
2. TextTest - see  [TextTest](https://texttest.org) for instructions for your platform
3. A lightweight editor like [Sublime Text](https://www.sublimetext.com/download)

You will want to configure TextTest to use the correct editor - see [How to Configure Default Editor and Diff Tool](https://texttest.org/how_to_guides/configure_editor.html)

Before you can run the tests you will need to create a virtual python environment and install some additional python packages in it that are needed by TextTest.

    python -m venv integration_tests/venv

Activate the virtual environment using the relevant script - this is the one for Windows Powershell:

    integration_tests/venv/Scripts/Activate.ps1

Install the additional python packages:

    pip install -r integration_tests/requirements.txt

This is needed so TextTest will be able to run the script integration_tests/test_rig.py. Start TextTest in this folder and you should open the static test browser. Select one or more tests from the left side, and run them.


## Swagger documentation
Alternative API documentation with Swagger can be found on [Swagger](https://localhost:3001/api-docs). Swagger also allows you to actually make the calls directly in the interface.

## API
API details can be found on the [api docs](https://localhost:3001/) (when you have it running locally).
