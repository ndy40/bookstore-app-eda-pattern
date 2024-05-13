import dataclasses
from enum import Enum

from bookstore.core.domain.value_objects import ValueObject


@dataclasses.dataclass
class Name(str):
    def __new__(cls, name):
        return super().__new__(cls, name.strip())


@dataclasses.dataclass
class Author(ValueObject):
    first_name: str
    last_name: str


@dataclasses.dataclass
class StatusAttribute(ValueObject):
    total_quantity: int | None = 0
    available_quantity: int | None = None


class BookCoverType(Enum):
    PAPER_BACK = "paper-back"
    HARD_COVER = "hard-cover"


@dataclasses.dataclass
class BookType(ValueObject):
    number_of_pages: int
    cover_type: BookCoverType
