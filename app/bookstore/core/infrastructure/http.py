from fastapi import FastAPI

from bookstore.core.infrastructure.graphql import graphql_router

app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")
