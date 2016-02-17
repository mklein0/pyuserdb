
DESC KEYSPACE demo;

CREATE KEYSPACE demo WITH replication = {
  'class': 'SimpleStrategy',
	  'replication_factor': '2'
};

CREATE TABLE users (
firstname text, 
lastname text, 
age int, 
email text, 
city text, 
PRIMARY KEY (lastname));

DESCRIBE TABLE users;


