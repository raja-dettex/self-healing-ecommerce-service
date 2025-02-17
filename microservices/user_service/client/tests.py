import grpc
from microservices.commons import users_pb2, users_pb2_grpc

channel = grpc.insecure_channel("localhost:50052")
stub = users_pb2_grpc.UserServiceStub(channel=channel)


def get_all_users():
    request = users_pb2.Empty()
    response = stub.get_users(request)

    print("responses " + str(response))


def del_user():
    request = users_pb2.UserId(id=2)
    response = stub.delete_user(request)
    print(str(response))


def add_user():
    request = users_pb2.User(id = 3, username='demo', email='demo', orders=[])
    response = stub.add_user(request)
    print(str(response))


add_user()
del_user()
get_all_users()
