from typing import List

from bookstore.core.infrastructure.graphql.types import ErrorMessage
from bookstore.core.infrastructure.publisher import publish
from bookstore.modules.book_mgt import services
from bookstore.modules.book_mgt.gql.types import (
    BookFailure,
    BookSuccess,
)
from . import types
from .data_mapper import book_mapper
from ..commands import CreateBook


def create_book(title: str, author: types.AuthorInput) -> BookSuccess | BookFailure:
    try:
        cmd = CreateBook(
            title=title,
            author_first_name=author.first_name,
            author_last_name=author.last_name,
            dob=author.dob,
        )
        book = publish(cmd, return_result=True)
        return BookSuccess(data=book_mapper.map_from_domain_to_gql(book))
    except Exception as e:
        return BookFailure(
            message=[ErrorMessage(title="book create", message=str(e))],
        )


def get_books() -> List[types.Book]:
    return [book_mapper.map_from_domain_to_gql(book) for book in services.get_books()]
