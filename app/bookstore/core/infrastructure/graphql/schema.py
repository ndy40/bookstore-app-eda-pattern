import strawberry

from bookstore.modules.book_mgt.gql.mutations import BookMgtMutation
from bookstore.modules.book_mgt.gql.queries import BookMgtQuery


@strawberry.type
class Mutation(BookMgtMutation):
    pass


@strawberry.type
class Query(BookMgtQuery):
    pass
