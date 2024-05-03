import strawberry
from strawberry.fastapi import GraphQLRouter

from bookstore.core.infrastructure.graphql.schema import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_router = GraphQLRouter(
    schema=schema,
)
