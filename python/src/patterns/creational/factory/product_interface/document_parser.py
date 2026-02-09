from abc import ABC, abstractmethod

class DocumentParser(ABC):
    @abstractmethod
    def parse(self, document: str) -> None:
        pass
