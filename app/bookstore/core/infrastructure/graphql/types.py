from typing import TypeVar, List, ClassVar

import strawberry

T = TypeVar("T")


@strawberry.interface
class Entity:
    id: strawberry.ID


@strawberry.interface
class Result:
    success: bool


@strawberry.interface
class Success(Result):
    success: bool = True


@strawberry.type
class ErrorMessage:
    title: str
    message: str


@strawberry.interface
class Failure(Result):
    success: bool = False
    message: List[ErrorMessage]
    model: ClassVar
