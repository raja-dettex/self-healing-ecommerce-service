import grpc
from microservices.commons import orders_pb2, orders_pb2_grpc

channel = grpc.insecure_channel("localhost:50053")
stub = orders_pb2_grpc.OrderServiceStub(channel=channel)


def get_all_orders():
    request = orders_pb2.Empty()
    response = stub.get_orders(request)

    print("responses " + str(response))


def del_user():
    request = orders_pb2.OrderId(id=2)
    response = stub.delete_order(request)
    print(str(response))


def add_order():
    request = orders_pb2.Order(
        id=1,
        product_name='iphone',
        qty=1,
        price=1500,
        total_price=1500,
        user_id=1
    )
    response = stub.add_order(request)
    print(str(response))


add_order()
add_order()
get_all_orders()
