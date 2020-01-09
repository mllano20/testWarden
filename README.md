# testWarden
Test de conocimientos back-end
Test Python Backend Developer

Answer the questions, it is allowed to research or use any material. Any code question refers to the Python 3 language. 

PART 1. 

    1. Mention a mechanism to integrate two or more Python applications. 
       
       It's possible to use modules and the import command to integrate two or more Python applications.
       
    2. What is a “stateless” service? 

	A stateless service is a service that treats each request as an independent transaction unrelated to previous requests.

PART 2. 

    1. Which design pattern allows any number of Python objects to communicate among them while ensuring low-coupling?

The design pattter that allows python objects to communicate while ensuring low-coupling is the “Mediator” design pattern, which is a type of Behavioral design pattern.

    2. Consider this example: A module that compiles and prints a report. Imagine such a module can be changed for two reasons. First, the format of the report could change. Second, the content of the report could change. These two things change for very different causes; one substantive, and one cosmetic. It would be a bad design to couple two things that change for different reasons at different times. What is the design principle discussed in this example? 

The design principle discussed above is the “Single esponsibility principle”.


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

