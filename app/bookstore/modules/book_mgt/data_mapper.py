from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic

from bookstore.core.domain.models import Entity
from bookstore.core.infrastructure.graphql.types import Entity as GQlEntity
from bookstore.modules.book_mgt import domain
from bookstore.modules.book_mgt.events import BookCreated
from bookstore.modules.book_mgt.gql.types import (
    Resource,
    Author,
    BookType as GqlBookType,
)
from bookstore.modules.book_mgt.value_objects import BookType

MapperEntity = TypeVar("MapperEntity", bound=Entity)
MapperModel = TypeVar("MapperModel", bound=Any)
GQLEntity = TypeVar("GQLEntity", bound=GQlEntity)


class _GQLDataMapper(Generic[MapperEntity, GQLEntity], ABC):
    domain_class: type[MapperEntity]
    gql_type_class: type[GQLEntity]

    @abstractmethod
    def map_from_domain_to_gql(self, domain: MapperEntity) -> GQLEntity:
        raise NotImplementedError

    @abstractmethod
    def map_from_gql_to_domain(self, gql: GQLEntity) -> MapperEntity:
        raise NotImplementedError


class GqlBookMapper(_GQLDataMapper[Resource, domain.Book]):
    def map_from_gql_to_domain(self, gql: Resource) -> domain.Book:
        return domain.Book(
            id=gql.id,
            title=gql.title,
            author=domain.Author(
                first_name=gql.author.first_name,
                last_name=gql.author.last_name,
            ),
            quantity=gql.quantity,
            media_type=BookType(
                number_of_pages=gql.media_type.number_of_pages,
                cover_type=gql.media_type.cover_type,
            ),
        )

    def map_from_domain_to_gql(self, domain: domain.Book) -> Resource:
        media_type = None

        if hasattr(domain, "media_type"):
            media_type = GqlBookType(
                number_of_pages=domain.media_type.number_of_pages,
                cover_type=domain.media_type.cover_type,
            )

        return Resource(
            id=domain.id,
            title=domain.title,
            author=[
                Author(
                    first_name=author.first_name,
                    last_name=author.last_name,
                )
                for author in domain.author
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
            author=[
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
