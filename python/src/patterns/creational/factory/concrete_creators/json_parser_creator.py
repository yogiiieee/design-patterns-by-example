from src.patterns.creational.factory.abstract_creator.parser_creator import ParserCreator
from src.patterns.creational.factory.concrete_products.json_parser import JsonParser
from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class JsonParserCreator(ParserCreator):
    def create_parser(self) -> DocumentParser:
        return JsonParser()
