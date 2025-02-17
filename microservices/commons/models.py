from typing import List

class Order:
    id: int
    product_name: str
    price: int
    qty: int
    total_price: int
    user_id: int
    def __init__(self, id: int, product_name: str, price: int , qty: int, user_id: int):
        self.id = id
        self.product_name = product_name
        self.price = price
        self.qty = qty
        self.total_price = price * qty
        self.user_id = user_id



class User:
    id: int
    username: str
    email: str
    orders: List[Order]

    def __init__(self, id: int, username: str, email: str, orders: List[Order]):
        self.id = id
        self.username = username
        self.email = email
        self.orders = orders


