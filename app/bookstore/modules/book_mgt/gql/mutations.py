import strawberry
from strawberry.tools import create_type

from bookstore.modules.book_mgt.gql import resolvers
from bookstore.modules.book_mgt.gql.types import BookSuccess, BookFailure

create_book: BookSuccess | BookFailure = strawberry.field(
    name="create_book", resolver=resolvers.create_book
)


BookMgtMutation = create_type(
    "BookMgtMutation",
    [
        create_book,
    ],
)
