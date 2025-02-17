from microservices.commons import orders_pb2_grpc, orders_pb2, models
from microservices.orders.repo.orders_repo import OrderRepo


class OrderService(orders_pb2_grpc.OrderServiceServicer):
    def __init__(self):
        self.repo: OrderRepo = OrderRepo()

    def add_order(self, request, context):
        order = models.Order(id=request.id,
                            product_name=request.product_name,
                            qty=request.qty,
                            price = request.price,
                            user_id=request.user_id)
        self.repo.add_order(order)
        return orders_pb2.Order(id=order.id,
                                product_name=order.product_name,
                                qty=order.qty,
                                price=order.price,
                                user_id=order.user_id)

    def get_orders(self, request, context):
       print("here")
       orders = self.repo.get_orders()
       return orders_pb2.OrderList(
           order = [orders_pb2.Order(id=order.id,
                                product_name=order.product_name,
                                qty=order.qty,
                                price=order.price,
                                user_id=order.user_id) for order in orders]
       )

    def delete_order(self, request, context):
        id = self.repo.remove_order(request.id)
        return orders_pb2.OrderId(id=id)

