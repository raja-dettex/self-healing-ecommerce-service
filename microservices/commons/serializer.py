from . import users_pb2, orders_pb2
import json
class Serializer:

    @staticmethod
    def serialize_users_list( users_list: users_pb2.UserList) -> str:
        users = [{"id" : u.id,
                              "username": u.username,
                              "email" : u.email,
                              "orders": [{
                                "id" : order.id,
                                "product_name": order.product_name,
                                "qty": order.qty,
                                "price": order.price,
                                "total_price": order.total_price,
                                "user_id": order.user_id
                              } for order in u.orders ]} for u in users_list.user]
        return json.dumps(users)

    @staticmethod
    def serialize_user(user: users_pb2.User) -> str:
        user_dic = {"id" : user.id,
                              "username": user.username,
                              "email" : user.email,
                              "orders": [{
                                "id" : order.id,
                                "product_name": order.product_name,
                                "qty": order.qty,
                                "price": order.price,
                                "total_price": order.total_price,
                                "user_id": order.user_id
                              } for order in user.orders ]}
        return json.dumps(user_dic)

    @staticmethod
    def serialize_order_list(order_list : orders_pb2.OrderList) -> str:
        if len(order_list.order) == 0:
            return json.dumps([])
        orders = [{
                                "id" : order.id,
                                "product_name": order.product_name,
                                "qty": order.qty,
                                "price": order.price,
                                "total_price": order.total_price,
                                "user_id": order.user_id
                              } for order in order_list.order ]
        return json.dumps(orders)

    @staticmethod
    def serialize_order(order: orders_pb2.Order) -> str:
        order_dict = {
                                "id" : order.id,
                                "product_name": order.product_name,
                                "qty": order.qty,
                                "price": order.price,
                                "total_price": order.total_price,
                                "user_id": order.user_id
                              }
        return json.dumps(order_dict)
