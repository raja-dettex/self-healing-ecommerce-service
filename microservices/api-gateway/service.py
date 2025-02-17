import json
import grpc
import api_gateway_pb2, api_gateway_pb2_grpc
from microservices.commons import orders_pb2_grpc, orders_pb2, serializer,  users_pb2_grpc, users_pb2

class APIGatewayService(api_gateway_pb2_grpc.APIGatewayServiceServicer):
    def RouteRequest(self, request, context):
        print("here")
        service_name = request.service_name
        try:
            data = json.loads(request.payload)  # Parse the JSON payload
        except json.JSONDecodeError:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Invalid JSON payload")
            return api_gateway_pb2.RouteResponseMessage(response="Invalid payload format")
        if service_name == "user-service":
            users_channel = grpc.insecure_channel("localhost:50052")
            usersStub = users_pb2_grpc.UserServiceStub(users_channel)
            if "action" in data:
                action = data["action"].lower()
                if action == "get":
                    response: users_pb2.UserList = usersStub.get_users(users_pb2.Empty())
                    users_str = serializer.Serializer.serialize_users_list(users_list=response)
                    return api_gateway_pb2.RouteResponseMessage(response=users_str)
                elif action == "create":
                    user = users_pb2.User(id=data["id"], username=data["username"], email=data["email"], orders=data["orders"])
                    print(user)
                    response = usersStub.add_user(user)
                    user_str = serializer.Serializer.serialize_user(user=response)
                    return api_gateway_pb2.RouteResponseMessage(response=user_str)
                elif action == "delete":
                    response: users_pb2.User = usersStub.delete_user(users_pb2.UserId(id=data["id"]))
                    user_str = serializer.Serializer.serialize_user(user=response)
                    return api_gateway_pb2.RouteResponseMessage(response=user_str)
            else:
                return api_gateway_pb2.RouteResponseMessage(response="invalid action")
        elif service_name == "order-service":
            orders_channel = grpc.insecure_channel("localhost:50053")
            ordersStub = orders_pb2_grpc.OrderServiceStub(channel=orders_channel)
            if "action" in data:
                action = data["action"].lower()
                if action == "get":
                    response: orders_pb2.OrderList = ordersStub.get_orders(orders_pb2.Empty())
                    orders_str = serializer.Serializer.serialize_order_list(order_list=response)
                    return api_gateway_pb2.RouteResponseMessage(response=orders_str)
                elif action == "create":
                    order = orders_pb2.Order(id=data["id"],
                                             product_name=data["product_name"],
                                             qty = data["qty"],
                                             price=data["price"],
                                             total_price=data["qty"] * data["price"],
                                             user_id=data["user_id"]
                                          )
                    print(order)
                    response = ordersStub.add_order(order)
                    order_str = serializer.Serializer.serialize_order(order=response)
                    return api_gateway_pb2.RouteResponseMessage(response=order_str)
                elif action == "delete":
                    response: orders_pb2.OrderId = ordersStub.delete_order(users_pb2.UserId(id=data["id"]))
                    return api_gateway_pb2.RouteResponseMessage(response=json.dumps({"order_id" : response.id}))
            else:
                return api_gateway_pb2.RouteResponseMessage(response="invalid action")

        else:
            return api_gateway_pb2.RouteResponseMessage(response="not implemented yet")
