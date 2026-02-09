from abc import ABC, abstractmethod
from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class ParserCreator(ABC):
    @abstractmethod
    def create_parser(self) -> DocumentParser:
        pass

    def parse(self, document: str) -> None:
        parser = self.create_parser()
        parser.parse(document)
