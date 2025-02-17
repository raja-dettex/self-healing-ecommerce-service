from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Order(_message.Message):
    __slots__ = ("id", "product_name", "qty", "price", "total_price", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    QTY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PRICE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    product_name: str
    qty: int
    price: int
    total_price: int
    user_id: int
    def __init__(self, id: _Optional[int] = ..., product_name: _Optional[str] = ..., qty: _Optional[int] = ..., price: _Optional[int] = ..., total_price: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class OrderId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class OrderList(_message.Message):
    __slots__ = ("order",)
    ORDER_FIELD_NUMBER: _ClassVar[int]
    order: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, order: _Optional[_Iterable[_Union[Order, _Mapping]]] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
