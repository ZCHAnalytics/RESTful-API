PostreSQL


1. Check connection to PostgreSQL using SQL Shell:
```
Server [localhost]: <default>
Database [postgres]: <default> 
Port [5432]: <default>
Username [postgres]: <default>
Password for user postgres: <password>
SELECT version();


2. Create a new database
CREATE DATABASE <database name>

![alt text](images/image-5.png)


checking if the database exists:
![alt text](images/image-6.png)

2. Create env file 
- create file and add connection string to the new database

![alt text](images/image-2.png)


ALTERNATIVE. Create database on render.com (free tier, availalbe for one month only)
- Create database restapi_database 
- copy connection string to .env file 
- add .env to .gitignore
- check connection with `python app.py`

![alt text](images/image-3.png)



