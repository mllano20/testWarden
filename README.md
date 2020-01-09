# testWarden
Test Python Backend Developer

PART 3. 

    1. Develop a web API to receive and store JSON messages.
    2. Technologies to be used:
        a. Python 
        b. Google AppEngine standard environment. 
        c. Google Data Store as DB NoSQL.
    3. General process:
        a. The server receives an API request in the route /push. Refer to https://www.w3schools.com/python/ref_requests_post.asp for an example of the client-side request.
        b. The server parses the json and checks the format.
        c. The server saves the json object in the entity “messages” in DataStore, each json field in the corresponding entity property.

URL of the web API:
https://testwarden.appspot.com

'/' : Answers to part 1 and 2 of the test
'/entries': get request that returns every entry stored in the google google datastore DB
'/push': post request that stores a new entry in the database, I used Postman to post the request to the server
