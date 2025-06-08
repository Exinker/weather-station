from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')


class SensorABC(ABC, Generic[T]):

    @property
    @abstractmethod
    def title(self) -> str:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def value() -> T:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def format(cls, value: T) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.format(self.value())
