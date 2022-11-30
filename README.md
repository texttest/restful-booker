# restful-booker
A simple Node booking form for testing RESTful web services.

## Installation
1. Ensure mongo is up and running by executing ```mongod``` in your terminal
2. Clone the repo
3. Navigate into the restful-booker root folder
4. Run ```npm install```
5. Run ```npm start```

## API
API details can be found on the [api docs](https://localhost:3001/) (when you have it running locally).

## Swagger documentation
Alternative API documentation with Swagger can be found on [Swagger](https://localhost:3001/api-docs). Swagger also allows you to actually make the calls directly in the interface.

## TextTests

This branch has some tests written using [TextTest](http://texttest.org). Start the texttest GUI:

    texttest
    
Select and run tests. 

You can record new tests also by selecting the "Record" option on the Running tab. Swagger then comes up, you can press "try it out" and make the call you want to make. 

To record the state of the database at the end of the test, check the "database setup run" button. This will create a "mongodata" folder in the test, you can then replace the actions in the test with actions that use that data.
