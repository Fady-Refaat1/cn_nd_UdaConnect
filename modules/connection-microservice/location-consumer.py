import os
from kafka import KafkaConsumer
from typing import List
from geoalchemy2.functions import ST_Point
from app.udaconnect_connection.models import  Location
from app import db

KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]

consumer = KafkaConsumer(KAFKA_TOPIC)
for message in consumer:
    location = message.value.decode("UTF-8")
    new_location = Location()
    new_location.person_id = location["person_id"]
    new_location.creation_time = location["creation_time"]
    new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
    print(new_location)
    db.session.add(new_location)
    db.session.commit()
    locations: List = db.session.query(Location).all()
