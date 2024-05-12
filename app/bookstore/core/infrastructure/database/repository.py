from abc import abstractmethod, ABCMeta
from typing import TypeVar, Any, Generic, List

from bunnet import init_bunnet
from pymongo import MongoClient

from bookstore.core.domain.models import Entity as DomainEntity
from bookstore.core.domain.value_objects import EntityUUID
from bookstore.core.infrastructure.data_mapper import (
    DataMapper,
)

Entity = TypeVar("Entity", bound=DomainEntity)
EntityId = TypeVar("EntityId", bound=EntityUUID)
BaseModel = TypeVar("BaseModel", bound=Any)


class _BaseRepository(Generic[EntityId, Entity], metaclass=ABCMeta):
    @abstractmethod
    def persist(self, entity: Entity) -> None: ...

    # @abstractmethod
    # def remove(self, entity: EntityId):
    #     ...
    #
    # @abstractmethod
    # def get_by_id(self, entity_id: EntityId) -> Entity:
    #     ...

    @abstractmethod
    def all(self) -> List[Entity]: ...


class EntityRepository(_BaseRepository[EntityId, Entity], metaclass=ABCMeta):
    mapper_class: type[DataMapper[Entity, BaseModel]]
    model_class: type[Entity]
    active_model = BaseModel

    def __init__(self, client: MongoClient):
        self.client = client
        init_bunnet(database=client.book_store, document_models=[self.model_class])

    def all(self) -> List[BaseModel]:
        return [
            self.mapper_class().map_from_model_to_entity(item)
            for item in self.active_model.find()
        ]

    def persist(self, entity: Entity) -> None:
        entity = self.mapper_class().map_from_entity_to_model(entity)
        entity.insert()

    def _map_model_to_entity(self, instance: BaseModel) -> Entity:
        assert self.mapper_class
        return self.mapper_class().map_from_model_to_entity(instance)

    def _map_entity_to_model(self, instance: Entity) -> BaseModel:
        assert self.mapper_class, (
            f"No model_class attribute set for {self.__class__.__name__}."
            "Make sure to include `model_class=MyModel` in the class."
        )
        return self.mapper_class.map_from_entity_to_model(instance)
