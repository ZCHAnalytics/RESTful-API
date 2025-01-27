import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request
from datetime import datetime, timezone


# Queries for creating tables
CREATE_ROOMS_TABLE = (
    "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"
)
CREATE_TEMPS_TABLE = """CREATE TABLE IF NOT EXISTS temperatures (room_id INTEGER, temperature REAL, 
                        date TIMESTAMP, FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE);"""

INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"
INSERT_TEMP = (
    "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"
)
GLOBAL_NUMBER_OF_DAYS = (
    """SELECT COUNT(DISTINCT DATE(date) AS days FROM temperatures;"""
)
GLOBAL_AVG = """SELECT AVG(temprature) as average FROM temperatures;"""


#Adding search queries:
ROOM_NAME = """SELECT name FROM rooms WHERE id = (%s)"""
ROOM_NUMBER_OF_DAYS = """SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures WHERE room_id = (%s);"""
ROOM_ALL_TIME_AVG = (
    "SELECT AVG(temperature) as average FROM temperatures WHERE room_id = (%s);"
)

#Load environment variables 
load_dotenv() 

app = Flask(__name__)
# Get database connection URL
url = os.getenv("DATABASE_URL") 

# Ensure tables are created when the app starts
try:
    connection = psycopg2.connect(url)
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(CREATE_TEMPS_TABLE)
    print("Tables are created successfully!")

except Exception as e:
    print("Could not create tables", e)
    connection = None 

# Rules for the app to handle requests

@app.post("/api/room")
# define endpoint  
def create_room(): 
    if connection is None:
        return {"error": "Database connection is not avaialble."}, 500
    
    data = request.get_json() # Get JSON data and turn it into dictionary
    name = data["name"] # Match the relevant key 
    with connection: # Use global connection 
        with connection.cursor() as cursor: # use context manager and cursor to interact with the database 
            cursor.execute(INSERT_ROOM_RETURN_ID, (name))
            room_id = cursor.fetchone()[0] # Return first column of the first row
    return {"id": room_id, "message": f"Room {name} created."}, 201 # status code "Created" to be sent to the client

# define endpoint
def add_temp():
    if connection is None:
        return {"error": "No connection is availalbe."}, 500
    data = request.get_json()
    temperature = data["temperature"]
    room_id = data["room"]

    try: 
        data = datetime.strptime(data["date"], "%m-%d-Y% %H:%M:%S")
    except KeyError:
        date = datetime.now(timezone.utc)
    
    with connection: # Global connection
        with connection.cursor() as cursor: # Context manager
            cursor.execute(INSERT_TEMP, (room_id, temperature, date))
    return {"message": "Temperature added."}, 201

# define endpoint for search queries
@app.get("/api/room/<int:room_id>")
def get_room_all(room_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ROOM_NAME, (room_id,))
            name = cursor.fetchone()[0]
            cursor.execute(ROOM_ALL_TIME_AVG, (room_id,))
            average = cursor.fetchone()[0]
            cursor.execute(ROOM_NUMBER_OF_DAYS, (room_id,))
            days = cursor.fetchone()[0]
    return {"name": name, "average": round(average, 2), "days": days}

