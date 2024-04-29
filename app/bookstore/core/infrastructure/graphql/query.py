from typing import List

import strawberry

from bookstore.core.infrastructure.graphql.types import Book, Author


def get_books():
    return [
        Book(title="book1", author=Author(first_name="Andrew", last_name="Coal")),
    ]


@strawberry.type
class Query:
    books: List[Book] = strawberry.field(resolver=get_books)
