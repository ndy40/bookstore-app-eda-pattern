import sys
from typing import List

from bookstore.core.infrastructure.bus.commands import command_bus
from bookstore.core.infrastructure.graphql.types import ErrorMessage
from bookstore.modules.book_mgt import services, domain

from bookstore.modules.book_mgt.gql.types import (
    BookType as GqlBookType,
    BookFailure,
    BookSuccess,
    Resource,
    AuthorInput,
    MediaInputType,
)

from ..commands import CreateBook
from ..data_mapper import _GQLDataMapper
from ..events import BookCreated
from ..value_objects import Author, BookType


class GqlBookMapper(_GQLDataMapper[Resource, domain.Book]):
    def map_from_gql_to_domain(self, gql: Resource) -> domain.Book:
        return domain.Book(
            id=gql.id,
            title=gql.title,
            authors=[domain.Author(
                first_name=author.first_name,
                last_name=author.last_name,
            ) for author in gql.authors],
            quantity=gql.quantity,
            media_type=BookType(
                number_of_pages=gql.media_type.number_of_pages,
                cover_type=gql.media_type.cover_type,
            ),
        )

    def map_from_domain_to_gql(self, obj: domain.Book) -> Resource:
        media_type = None

        if media:= getattr(obj, "media_type"):
            media_type = GqlBookType(
                number_of_pages=media.number_of_pages,
                cover_type=media.cover_type,
            )
        print(obj.authors)

        return Resource(
            id=obj.id,
            title=obj.title,
            authors=[
                Author(
                    first_name=author.first_name,
                    last_name=author.last_name,
                )
                for author in obj.authors
            ],
            media_type=media_type,
        )


class GqlBookCreatedEventMapper(_GQLDataMapper[Resource, BookCreated]):

    def map_from_domain_to_gql(self, domain: BookCreated) -> Resource:
        media_type = None

        if domain.media_type:
            media_type = GqlBookType(
                number_of_pages=domain.media_type.number_of_pages,
                cover_type=domain.media_type.cover_type,
            )

        return Resource(
            id=domain.id,
            title=domain.title,
            authors=[
                Author(
                    first_name=author.first_name,
                    last_name=author.last_name,
                )
                for author in domain.author
            ],
            media_type=media_type,
        )

    def map_from_gql_to_domain(self, gql: Resource) -> BookCreated:
        raise NotImplementedError


book_mapper = GqlBookMapper()
book_event_mapper = GqlBookCreatedEventMapper()


def create_book(
        title: str,
        authors: List[AuthorInput],
        summary: str,
        media_type: MediaInputType,
        quantity: int = 1,
) -> BookSuccess | BookFailure:
    try:
        cmd = CreateBook(
            title=title,
            author=[Author(first_name=author.first_name, last_name=author.last_name) for author in authors],
            quantity=quantity,
            summary=summary,
            # media_type=BookType(
            #     number_of_pages=media_type.number_of_pages,
            #     cover_type=media_type.cover_type.value,
            # )
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


def get_books() -> List[Resource]:
    return [book_mapper.map_from_domain_to_gql(book) for book in services.get_books()]
