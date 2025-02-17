from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RouteRequestMessage(_message.Message):
    __slots__ = ("service_name", "payload")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    payload: str
    def __init__(self, service_name: _Optional[str] = ..., payload: _Optional[str] = ...) -> None: ...

class RouteResponseMessage(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...
