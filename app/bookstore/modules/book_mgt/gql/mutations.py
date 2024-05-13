import strawberry
from strawberry.tools import create_type

from bookstore.modules.book_mgt.gql import resolvers

create_book = strawberry.field(
    name="create_book", resolver=resolvers.create_book
)


BookMgtMutation = create_type(
    "BookMgtMutation",
    [
        create_book,
    ],
)
