import strawberry
from strawberry.fastapi import GraphQLRouter

from bookstore.core.infrastructure.graphql.mutations import Mutations
from bookstore.core.infrastructure.graphql.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutations)
graphql_router = GraphQLRouter(
    schema=schema,
)
