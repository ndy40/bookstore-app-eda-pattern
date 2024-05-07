import dataclasses

from bookstore.core.domain.value_objects import ValueObject


@dataclasses.dataclass
class Name(str, ValueObject):
    def __new__(cls, name):
        return super().__new__(cls, name.strip())


@dataclasses.dataclass
class Author(ValueObject):
    first_name: Name
    last_name: Name


@dataclasses.dataclass
class StatusAttribute(ValueObject):
    total_quantity: int | None = 0
    available_quantity: int | None = None
