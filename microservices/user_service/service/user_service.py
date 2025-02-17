from microservices.commons import users_pb2_grpc, users_pb2, models
from microservices.user_service.repo.user_repo import UserRepo


class UserService(users_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.repo : UserRepo = UserRepo()

    def add_user(self, request, context):
        user = models.User(id=request.id, username=request.username,email=request.email, orders=request.orders)
        self.repo.add_user(user)
        return users_pb2.User(id=user.id, username=user.username, email=user.email, orders=user.orders)

    def get_users(self, request, context):
       print("here")
       users = self.repo.get_users()
       return users_pb2.UserList(
           user = [users_pb2.User(id=user.id, username=user.username, email=user.email, orders=user.orders) for user in users]
       )

    def delete_user(self, request, context):
        print(request.id)
        user = self.repo.remove_user(request.id)
        print
        return users_pb2.User(id=user.id, username=user.username, email=user.email, orders=user.orders)
