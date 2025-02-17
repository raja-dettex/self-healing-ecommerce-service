import grpc
from concurrent import futures
import sys
import os


from microservices.orders.service.order_service import OrderService
from microservices.commons.orders_pb2_grpc import add_OrderServiceServicer_to_server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port("[::]:50053")
    server.start()
    print("started")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
