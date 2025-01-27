We want to run these three quesries:

1. Write SQL queires:
# Get the name of the room
SELECT name FROM rooms WHERE id = (%s);

# Get all time average 
SELECT AVG(temperature) as average FROM temperature WHERE room_id = (%s);

# Calculate how many dayts of data are stored for the room
SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperature WHERE room_id = (%s);


2. Add them as constants in app.py 

