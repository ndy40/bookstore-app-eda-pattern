import datetime

import strawberry

from bookstore.core.infrastructure.graphql.types import Success, Failure, Entity


@strawberry.input
class AuthorInput:
    first_name: str
    last_name: str
    dob: datetime.date | None = None


@strawberry.type
class Author:
    first_name: str
    last_name: str
    dob: datetime.date | None = None


@strawberry.type
class Book(Entity):
    title: str
    author: Author


@strawberry.type
class BookSuccess(Success):
    data: Book


@strawberry.type
class BookFailure(Failure):
    model = Book
