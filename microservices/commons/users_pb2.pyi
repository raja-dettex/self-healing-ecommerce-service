import orders_pb2 as _orders_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "username", "email", "orders")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    email: str
    orders: _containers.RepeatedCompositeFieldContainer[_orders_pb2.Order]
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., orders: _Optional[_Iterable[_Union[_orders_pb2.Order, _Mapping]]] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class UserList(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedCompositeFieldContainer[User]
    def __init__(self, user: _Optional[_Iterable[_Union[User, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
