import json
import os
import time
from concurrent import futures
from kafka import KafkaProducer
import grpc
import location_pb2
import location_pb2_grpc

KAFKA_URL= os.environ["KAFKA_URL"]
TOPIC_NAME = os.environ["KAFKA_TOPIC"]

producer = KafkaProducer(bootstrap_servers=KAFKA_URL)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message from grbc")
        request_value = {
            "userId" : int(request.userId),
            "latitude" : int(request.latitude),
            "longitude" : int(request.longitude)
        }
        location_encode_data = json.dumps(request_value, indent=2).encode('utf-8')
        producer.send(TOPIC_NAME, location_encode_data)
        producer.flush()
        return location_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
