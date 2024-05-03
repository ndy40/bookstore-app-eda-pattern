from typing import List

from bookstore.core.infrastructure.data_mapper import GQLDataMapper
from bookstore.core.infrastructure.graphql.types import ErrorMessage
from bookstore.modules.book_mgt import domain
from bookstore.modules.book_mgt import services
from bookstore.modules.book_mgt.gql import types
from bookstore.modules.book_mgt.gql.types import (
    BookFailure,
    BookSuccess,
)


class BookMapper(GQLDataMapper[types.Book, domain.Book]):
    def map_from_gql_to_domain(self, gql: types.Book) -> domain.Book:
        return domain.Book(
            id=gql.id,
            title=gql.title,
            author=domain.Author(
                first_name=gql.author.first_name,
                last_name=gql.author.last_name,
                dob=gql.author.dob,
            ),
        )

    def map_from_domain_to_gql(self, domain: domain.Book) -> types.Book:
        return types.Book(
            id=domain.id,
            title=domain.title,
            author=types.Author(
                first_name=domain.author.first_name,
                last_name=domain.author.last_name,
                dob=domain.author.dob,
            ),
        )


def create_book(title: str, author: types.AuthorInput) -> BookSuccess | BookFailure:
    try:
        new_book = services.create_new_book(
            title=title,
            author_first_name=author.first_name,
            author_last_name=author.last_name,
            dob=author.dob,
        )

        gql_model = BookMapper().map_from_gql_to_domain(new_book)
        return BookSuccess(data=gql_model)
    except Exception as e:
        return BookFailure(
            message=[ErrorMessage("book create", str(e))],
        )


def get_books() -> List[types.Book]:
    print(services.get_books())
    return [BookMapper().map_from_domain_to_gql(book) for book in services.get_books()]
