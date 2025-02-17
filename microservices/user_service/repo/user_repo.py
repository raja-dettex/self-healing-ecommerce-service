from microservices.commons.models import User
from typing import List


class UserRepo:
    users: List[User]

    def __init__(self):
        self.users = [
            User(1, 'user1', 'user1@gmail.com', []),
            User(2, 'user2', 'user2@gmail.com', [])
        ]
    def add_user(self, user: User):
        self.users.append(user)

    def get_by_id(self, id: int) -> User:
        return [user for user in self.users if user.id==id][0]

    def remove_user(self, user_id: int):
        user = self.get_by_id(user_id)
        self.users = [user for user in self.users if user.id != user_id]
        return user
    def get_users(self) -> List[User]:
        return self.users


