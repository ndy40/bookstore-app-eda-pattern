from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic

from bookstore.core.domain.models import Entity
from bookstore.core.infrastructure.graphql import types

MapperEntity = TypeVar("MapperEntity", bound=Entity)
MapperModel = TypeVar("MapperModel", bound=Any)

GQLEntity = TypeVar("GQLEntity", bound=types.Entity)


class DataMapper(Generic[MapperEntity, MapperModel], ABC):
    entity_class: type[MapperEntity]
    model_class: type[MapperModel]

    @abstractmethod
    def map_from_entity_to_model(self, entity: MapperEntity) -> MapperModel:
        raise NotImplementedError

    @abstractmethod
    def map_from_model_to_entity(self, model: MapperModel) -> MapperEntity:
        raise NotImplementedError


class GQLDataMapper(Generic[MapperEntity, GQLEntity]):
    domain_class: type[MapperEntity]
    gql_type_class: type[GQLEntity]

    @abstractmethod
    def map_from_domain_to_gql(self, domain: MapperEntity) -> GQLEntity:
        raise NotImplementedError

    @abstractmethod
    def map_from_gql_to_domain(self, gql: GQLEntity) -> MapperEntity:
        raise NotImplementedError
