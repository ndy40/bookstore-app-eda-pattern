from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic

from bookstore.core.domain.models import Entity
from bookstore.core.infrastructure.graphql.types import Entity as GQlEntity

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

