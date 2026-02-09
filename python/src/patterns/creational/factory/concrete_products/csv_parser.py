from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class CsvParser(DocumentParser):
    def parse(self, document: str) -> None:
        print(f"Parsing CSV document: {document}")
