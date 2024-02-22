# restful-booker
A simple Node booking form for testing RESTful web services.

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

## Unit Tests
There are some unit tests in the /tests folder. Run these tests:

    npm test

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

## API tests with Specmatic
These tests will check the actual api against the OpenAPI specification in [oas.yaml](oas.yaml). Before you can run these tests you will need to download [Specmatic](https://specmatic.in/). It comes in the form of a jar file so you will also need to install Java or a JRE in order to run it.

First start the application under test running:

    npm start

Then run specmatic to check the api complies with the spec:

    java -jar specmatic.jar test oas.yaml --testBaseURL=http://localhost:3001

## OpenAPI validator code
In app.js you can find some validation code using OpenApiValidator that will check the API matches the spec. This code is currenly only checking the responses match the specs, not the requests. If you want to check the reqeusts too, set 'validateRequests' to true.

## Exploratory testing
You can use the Swagger interface to explore the API. If you are a system administrator you will know the special Auth header that can be used for example to delete bookings:

    Basic YWRtaW46cGFzc3dvcmQxMjM=

## Running Specmatic Contract Tests

### Pre-requisites

Please ensure you have the latest Docker Desktop Install, the contract test using [testcontainers](testcontainers.org) to spin up a MongoDB for the test

### Running tests

    npm run contract-test