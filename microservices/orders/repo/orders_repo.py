from microservices.commons.models import Order
from typing import List


class OrderRepo:
    orders : List[Order]

    def __init__(self):
        self.orders = []
    def add_order(self, order: Order):
        self.orders.append(order)

    def remove_order(self, order_id: int) -> int:
        self.orders  = [order for order in self.orders if order.id != order_id]
        return order_id
    def get_orders(self) -> List[Order]:
        return self.orders


