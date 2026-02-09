from src.patterns.creational.factory.abstract_creator.parser_creator import ParserCreator
from src.patterns.creational.factory.concrete_products.xml_parser import XmlParser
from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class XmlParserCreator(ParserCreator):
    def create_parser(self) -> DocumentParser:
        return XmlParser()
