# DataStax Python Driver for Apache Cassandra Quickstart

A basic Python demo CRUD application using the DataStax Python Driver for Apache Cassandra. 
The intent is to help users get up and running quickly with the driver. 
If you are having trouble, the complete code solution for `quickstart.py` can be found [here](https://gist.github.com/beccam/c896674cc555e8857783f3fe91fbc8a0).

## Prerequisites
  * A running instance of [Apache Cassandra®](http://cassandra.apache.org/download/) 2.1+
  * [Python](https://www.python.org/downloads/) 2.7, 3.3, 3.4, 3.5, or 3.6.
  * Use Pip to install the driver: `pip install cassandra-driver`
  
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
