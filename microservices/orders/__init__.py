from microservices.commons.models import Order
from typing import List


class OrderRepo:
    def __init__(self):
        self.orders : List[Order] = []

    def add(self, order: Order) -> Order:
        self.orders.append(order)

    def remove(self, order_id: int) -> int:
        self.orders = [order for order in self.orders if order.id != order_id]
        return order_id

    def get(self) -> List[Order]:
        return self.orders
