from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class JsonParser(DocumentParser):
    def parse(self, document: str) -> None:
        print(f"Parsing JSON document: {document}")
