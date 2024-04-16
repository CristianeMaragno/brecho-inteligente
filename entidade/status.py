from abc import ABC, abstractmethod

class Status(ABC):
    @abstractmethod
    def __str__(self):
        pass