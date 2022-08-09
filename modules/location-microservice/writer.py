import grpc
import location_pb2
import location_pb2_grpc


"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("location-svc-api:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    userId = 16,
    latitude = 100000,
    longitude = 200000
)


response = stub.Create(location)
