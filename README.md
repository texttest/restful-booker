# restful-booker
A simple booking API for testing RESTful web services. The original version was designed by 
[Mark Winteringham](https://restful-booker.herokuapp.com/). This version has been modified
by Emily Bache and Geoffrey Bache to enable an approval testing approach using [TextTest](https://texttest.org).

## Installation
In order to run restful booker you will need to install:
1. npm and node
2. mongo db

From this folder you should then be able to execute:

    npm install
    npm start

Restful booker should then start running on [localhost](https://localhost:3001/) and you can access it from a browser.

## Swagger documentation
API documentation with Swagger can be found on [Swagger](https://localhost:3001/api-docs) when the application is running.

## Integration tests with TextTest
In order to run the [TextTest](https://texttest.org) integration tests in the folder 'integration_tests'
you will need to install:

1. Python
2. TextTest - see  [TextTest](https://texttest.org) for instructions for your platform
3. A lightweight editor like [Sublime Text](https://www.sublimetext.com/download)

You will want to configure TextTest to use the correct editor - see [How to Configure Default Editor and Diff Tool](https://texttest.org/how_to_guides/configure_editor.html)

When you are developing, updating and fixing tests, you will want to do this interactively with the TextTest GUI. Start it like this:

    cd integration_tests
    .\start_texttest.bat

or on posix:

    cd integration_tests
    ./start_texttest.sh

This should open the TextTest GUI. If you just want to run the tests non-interactively (eg on a build server) then you can pass the argument "-con" to just run the tests on the command line.

On this main branch there is only one test case, for 'ping', and it is not completed. The intention is that you use this branch as a starting point for an exercise to create tests for all the endpoints using TextTest. To view a complete set of sample tests, switch to the 'with_texttests' branch.

## Exploratory testing
You can use the Swagger interface to explore the API. If you are a system administrator you will know the special Auth header that can be used for example to delete bookings:

    Basic YWRtaW46cGFzc3dvcmQxMjM=
