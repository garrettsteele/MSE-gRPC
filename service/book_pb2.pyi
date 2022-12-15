from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "publishing_year", "title"]
    class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    FANTASY: Book.Genre
    HORROR: Book.Genre
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    ROMANCE: Book.Genre
    SCIFI: Book.Genre
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    publishing_year: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., publishing_year: _Optional[int] = ...) -> None: ...

class Create_book_reply(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: str
    def __init__(self, success: _Optional[str] = ...) -> None: ...

class Inventory_Item(_message.Message):
    __slots__ = ["ISBN", "author", "inventory_number", "publishing_year", "title"]
    class STATUS(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE: Inventory_Item.STATUS
    INVENTORY_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHING_YEAR_FIELD_NUMBER: _ClassVar[int]
    TAKEN: Inventory_Item.STATUS
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    inventory_number: int
    publishing_year: int
    title: str
    def __init__(self, inventory_number: _Optional[int] = ..., ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., publishing_year: _Optional[int] = ...) -> None: ...
