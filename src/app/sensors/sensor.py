from abc import ABC, abstractmethod
from typing import Generic, TypeVar


T = TypeVar('T')


class SensorABC(ABC, Generic[T]):

    @staticmethod
    def value() -> T:
        raise NotImplementedError

    @classmethod
    def format(cls, value: T) -> str:
        raise NotImplementedError

    def __str__(self) -> str:
        return self.format(self.value())
