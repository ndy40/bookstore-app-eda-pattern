from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from bookstore.core.infrastructure.data_mapper import MapperEntity
from bookstore.modules.book_mgt import domain
from . import types

GQLEntity = TypeVar("GQLEntity", bound=types.Entity)


class GQLDataMapper(Generic[MapperEntity, GQLEntity], ABC):
    domain_class: type[MapperEntity]
    gql_type_class: type[GQLEntity]

    @abstractmethod
    def map_from_domain_to_gql(self, domain: MapperEntity) -> GQLEntity:
        raise NotImplementedError

    @abstractmethod
    def map_from_gql_to_domain(self, gql: GQLEntity) -> MapperEntity:
        raise NotImplementedError


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


book_mapper = BookMapper()
