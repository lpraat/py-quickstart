from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol, runtime_checkable


@runtime_checkable
class CanTalk(Protocol):
    @abstractmethod
    def talk():
        ...


@dataclass(frozen=True)
class Human:
    name: str

    def talk(self):
        print(f"My name is {self.name}")
