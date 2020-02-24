# DataStax Python Driver for Apache Cassandra Quickstart

A basic Python demo CRUD application using the DataStax Python Driver for Apache Cassandra. 
Run the [quickstart_python.py](quickstart_python.py) file if you want to run the application with the complete code.

Contributors: [Rebecca Mills](https://github.com/beccam)

## Objectives

* To demonstrate how to perform basic CRUD operations with the DataStax Python Driver.
* The intent is to help users get up and running quickly with the driver. 

## How this Sample Works
This project walks through basic CRUD operations using Cassandra. The demo application will first insert a row of user data, select that same row back out, update the row and finally delete the user. The README includes the code snippets to be filled in to the main application code to complete the functionality.

## Project Layout

* [quickstart.py](quickstart.py) - main application file with space to fill in CRUD operation code
* [users.cql](users.cql) - Use this file to create the schema 

## Prerequisites
  * A running instance of [Apache Cassandra®](http://cassandra.apache.org/download/) 2.1+
  * [Python](https://www.python.org/downloads/) 2.7, 3.4, 3.5, or 3.6.
  * Use Pip to install the driver: `pip install cassandra-driver`
  * We highly recommend to use a virtualenv
  
  ## Create the keyspace and table
The `users.cql` file provides the schema used for this project:

```sql
CREATE KEYSPACE demo
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

CREATE TABLE demo.users (
    lastname text PRIMARY KEY,
    age int,
    city text,
    email text,
    firstname text);
```

## Connect to your cluster

All of our code is contained in the `quickstart.py` file. 
The `create_connection()` function connects to our cluster.
By default, `Cluster()` will try to connect to 127.0.0.1 (localhost). Replace with your own contact point(s) if necessary.

```python
def create_connection():
    # TO DO: Fill in your own contact point
    cluster = Cluster(['127.0.0.1'])
    return cluster.connect('demo')
```

## CRUD Operations
Fill the code in the functions that will add a user, get a user, update a user and delete a user from the table with the driver.

### INSERT a user
```python
def set_user(session, lastname, age, city, email, firstname):
    # TO DO: execute SimpleStatement that inserts one user into the table
    session.execute("INSERT INTO users (lastname, age, city, email, firstname) VALUES (%s,%s,%s,%s,%s)", [lastname, age, city, email, firstname])
```
### SELECT a user
```python
def get_user(session, lastname):
    # TO DO: execute SimpleStatement that retrieves one user from the table
    # TO DO: print firstname and age of user
    result = session.execute("SELECT * FROM users WHERE lastname = %s", [lastname]).one()
    print result.firstname, result.age
```

### UPDATE a user's age
```python
def update_user(session, new_age, lastname):
    # TO DO: execute SimpleStatement that updates the age of one user
    session.execute("UPDATE users SET age =%s WHERE lastname = %s", [new_age, lastname])
```   

### DELETE a user
```python
def delete_user(session, lastname):
    # TO DO: execute SimpleStatement that deletes one user from the table
    session.execute("DELETE FROM users WHERE lastname = %s", [lastname])
```
 ## License
Copyright 2019 Rebecca Mills

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.   

