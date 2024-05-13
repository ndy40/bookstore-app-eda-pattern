import sys
from typing import List

from bookstore.core.infrastructure.bus.commands import command_bus
from bookstore.core.infrastructure.graphql.types import ErrorMessage
from bookstore.modules.book_mgt import services
from bookstore.modules.book_mgt.data_mapper import (
    GqlBookMapper,
    GqlBookCreatedEventMapper,
)
from bookstore.modules.book_mgt.gql.types import (
    BookFailure,
    BookSuccess,
)
from . import types
from ..commands import CreateBook
from ..value_objects import Author, BookType

book_mapper = GqlBookMapper()
book_event_mapper = GqlBookCreatedEventMapper()


def create_book(
    title: str,
    author: types.AuthorInput,
    summary: str,
    media_type: types.MediaInputType,
    quantity: int = 1,
) -> BookSuccess | BookFailure:
    try:
        cmd = CreateBook(
            title=title,
            author=[Author(first_name=author.first_name, last_name=author.last_name)],
            quantity=quantity,
            summary=summary,
            media_type=BookType(
                number_of_pages=media_type.number_of_pages,
                cover_type=media_type.cover_type,
            ),
        )

        book = command_bus.execute(cmd)
        print("## book", type(book))
        return BookSuccess(data=book_event_mapper.map_from_domain_to_gql(book))
    except Exception as e:
        import traceback

        ex_info = sys.exc_info()
        print(traceback.print_exception(*ex_info))
        return BookFailure(
            message=[ErrorMessage(title="book create", message=str(e))],
        )


def get_books() -> List[types.Resource]:
    return [book_mapper.map_from_domain_to_gql(book) for book in services.get_books()]
