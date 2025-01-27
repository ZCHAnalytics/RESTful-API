1. Create a table if does not exit

Check if tables exist after rinning the command `python app.py`

- open psql shell and connect to the database: 
psql -U postgres -d rest_api_db 

run command `\dt`

Output:
rest_api_db=# \dt
            List of relations
 Schema |     Name     | Type  |  Owner
--------+--------------+-------+----------
 public | rooms        | table | postgres
 public | temperatures | table | postgres
(2 rows)




