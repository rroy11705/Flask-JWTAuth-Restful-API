# Enosis Fantastic

## Description

This is a Restful API using Flask and MongoDB.
The purpose of the API is user authentication using JWT.

* **Flask** is a lightweight web application framework designed to get results fast and leave room to make the app more detailed in the future.
   Here we do not having to follow a strict convention, hence it could accelerate the development process and gives developers the added flexibility.
   
* As a document database, **MongoDB** makes it easy for developers to store structured or unstructured data. It uses a JSON-like format to store documents. This format directly maps to native objects in most modern programming languages, making it a natural choice for developers, as they don’t need to think about normalizing data. MongoDB can also handle high volume and can scale both vertically or horizontally to accommodate large data loads.

---

## Pre-requisites
At least Python 3.6 installed. 
* [Installation guide on Windows](https://docs.python.org/3.6/using/windows.html)
* [Installation guide on Unix](https://docs.python.org/3.6/using/unix.html)
* [Installation guide on Macintosh](https://docs.python.org/3.6/using/mac.html)

---

## Getting Started

1. Clone the repository using:
    > git clone https://github.com/rroy11705/Student-Management-System-Flask.git

2. It is suggested to use a virtual environment.
    * To install virtualenv
        > pip install virtualenv
    * To create a virtualenv
        > virtualenv env_name
    * To activate virtualenv
        > source env_name/bin/activate (on linux or mac)
        > env_name/Scripts/activate (on windows)

3. Go to console, open the folder and install dependencies from _requirements.txt_ file using:
    > pip install -r requirements.txt

4. Make Sure you have mongodb installed and running. 
   You can refer to the [official installation guide of mongodb](https://docs.mongodb.com/manual/installation/).

5. Remane the _.exampleenv_ file to _.env_ and assign significant values to the environment variables

6. From console run the _run-app.py_ using:
    > python app.py

7. Use Postman to check the endpoints.

---

## Endpoints

### 1. /api/create-user \[method=GET\]
To create a user using POST method.

The Input format for this endpoint is:
![create-user-input](resources/create-user-input.png)

The Successful Output of this endpoint is:
![create-user-output](resources/create-user-output.png)

If email already exist then the output is:
![create-user-duplicate](resources/create-user-duplicate.png)


### 2. /auth/login \[method=POST\]
To log in using an existing email address and returns a Bearer token.


### 3. /auth/signup \[method=POST\]
To create a new user and store the user details to database.


### 3. /auth/reset_password \[method=PUT\]
To reset a password using an existing email address and existing password.


---

## LICENSE

[MIT License](https://github.com/rroy11705/Student-Management-System-Flask/blob/main/LICENSE)
Copyright (c) 2021 Rahul Roy