from datetime import date

import strawberry

from bookstore.core.infrastructure.graphql.types import Book, Author


@strawberry.input
class AuthorInput:
    first_name: str
    last_name: str
    dob: date | None = None


@strawberry.type
class Mutations:
    @strawberry.field
    def create_book(self, title: str, author: AuthorInput) -> Book:
        return Book(
            title=title,
            author=Author(first_name=author.first_name, last_name=author.last_name),
        )
