# Feature that returns a image from database
import grpc
from concurrent import futures
import Greet_pb2
import Greet_pb2_grpc
import logging

class Greeting(Greet_pb2_grpc.GreetingServicer):
    def SayHello(self, request, context):
        return Greet_pb2.HelloReply(message="Hello, %s!" % request.name)

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Greet_pb2_grpc.add_GreetingServicer_to_server(Greeting(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()