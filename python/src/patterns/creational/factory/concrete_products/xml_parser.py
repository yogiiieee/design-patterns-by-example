from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class XmlParser(DocumentParser):
    def parse(self, document: str) -> None:
        print(f"Parsing XML document: {document}")
