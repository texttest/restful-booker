# restful-booker
A simple booking API for testing RESTful web services. The original version was designed by 
[Mark Winteringham](https://restful-booker.herokuapp.com/). This version has been modified
by Emily Bache to enable an approval testing approach using [TextTest](http://texttest.org).

## Installation
1. Ensure mongo is up and running by executing ```mongod``` in your terminal
2. Clone this repo
3. Navigate into the restful-booker root folder
4. Run ```npm install```
5. Run ```npm start```

## API
API details can be found on the [api docs](https://localhost:3001/) (when you have it running locally).

## Emily's modifications
The original application designed by Mark Winteringham needed two modifications to enable an approval
testing approach.

1. Ability to populate the database with known data on startup:

    By default the application generates 10 random records in the database on startup. 
    If you set the environment variable LOAD_DB to true and set the environment variable DB_FILE to a filename then it 
    will use the contents to load those records into the database on startup.
    
1. Ability to write the contents of the database to a json file:

    There is an additional REST endpoint called 'Dump DB' which, if you call it, will write a json file
    to the local filesystem containing the current database contents. For full details,
    see the [Dump DB API Docs](http://localhost:3001/apidoc/index.html#api-Admin-DumpDB).

In addition, Emily has added a python script 'texttest_fixture.py' that enables data-driven testing. 
This script starts the application, runs one request-response cycle, then stops it again. 

## Tests
There is a skeleton test provided with [TextTest](http://texttest.org). Start the texttest GUI with:

    texttest
  
The idea is to add further, similar tests.  
If you want to see a full suite/sample solution, look in the 'with_texttests' branch


