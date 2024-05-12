from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic

from bookstore.core.domain.models import Entity
from bookstore.modules.book_mgt import domain
from bookstore.modules.book_mgt.gql import types

MapperEntity = TypeVar("MapperEntity", bound=Entity)
MapperModel = TypeVar("MapperModel", bound=Any)
GQLEntity = TypeVar("GQLEntity", bound=types.Entity)


class _GQLDataMapper(Generic[MapperEntity, GQLEntity], ABC):
    domain_class: type[MapperEntity]
    gql_type_class: type[GQLEntity]

    @abstractmethod
    def map_from_domain_to_gql(self, domain: MapperEntity) -> GQLEntity:
        raise NotImplementedError

    @abstractmethod
    def map_from_gql_to_domain(self, gql: GQLEntity) -> MapperEntity:
        raise NotImplementedError


class GqlBookMapper(_GQLDataMapper[types.Resource, domain.Book]):
    def map_from_gql_to_domain(self, gql: types.Resource) -> domain.Book:
        return domain.Book(
            id=gql.id,
            title=gql.title,
            author=domain.Author(
                first_name=gql.author.first_name,
                last_name=gql.author.last_name,
                dob=gql.author.dob,
            ),
        )

    def map_from_domain_to_gql(self, domain: domain.Book) -> types.Resource:
        return types.Resource(
            id=domain.id,
            title=domain.title,
            author=[
                types.Author(
                    first_name=author.first_name,
                    last_name=author.last_name,
                )
                for author in domain.author
            ],
            media_type=None,
        )
