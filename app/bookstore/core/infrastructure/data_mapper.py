from abc import ABC, abstractmethod
from typing import TypeVar, Any, Generic

from bookstore.core.domain.models import Entity

MapperEntity = TypeVar("MapperEntity", bound=Entity)
MapperModel = TypeVar("MapperModel", bound=Any)


class DataMapper(Generic[MapperEntity, MapperModel], ABC):
    entity_class: type[MapperEntity]
    model_class: type[MapperModel]

    @abstractmethod
    def map_from_entity_to_model(self, entity: MapperEntity) -> MapperModel:
        raise NotImplementedError

    @abstractmethod
    def map_from_model_to_entity(self, model: MapperModel) -> MapperEntity:
        raise NotImplementedError
