import grpc
from concurrent import futures
import sys
import os


from microservices.user_service.service.user_service import UserService
from microservices.commons.users_pb2_grpc import add_UserServiceServicer_to_server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    print("started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
