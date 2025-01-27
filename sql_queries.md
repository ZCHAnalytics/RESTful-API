# SQL Queries  

This document contains SQL commands used in the `app.py` file for creating and interacting with the database. 

## Table Creation Queries 
These queries ensure that the required tables exist in the database: 

```sql
CREATE TABLE IF NOT EXISTS rooms (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS temperatures (
    room_id INTEGER,
    temperature REAL,
    date TIMESTAMP,
    FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE
);
```

## Queries for Inserting Data

- Insert a new room and return its ID: 
```sql
INSERT INTO rooms (name) VALUES (%s) RETURNING id;
```

- Insert a temperature record:
```sql 
INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);
```

## Queries for Retrieving Data

- Get the name of a room:

```sql
SELECT name FROM rooms WHERE id = (%s);
```

- Calculate all-time average temperature: 
```sql
SELECT AVG(temperature) as average FROM temperature WHERE room_id = (%s);
```

- Calculate number of days of data for a room:
```sql
SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperature WHERE room_id = (%s);
```

## Verify Table Creation
After running the `python app.py` command, verify that the tables are created: 

- Open the PostgreSQL shell and connect to the database: 
`psql -U postgres -d rest_api_db` 
- List all tables in the database:
```sql
\dt
```

- Example output:
```
rest_api_db=# \dt
            List of relations
 Schema |     Name     | Type  |  Owner
--------+--------------+-------+----------
 public | rooms        | table | postgres
 public | temperatures | table | postgres
(2 rows)
```
