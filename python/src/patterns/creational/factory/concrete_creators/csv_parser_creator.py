from src.patterns.creational.factory.abstract_creator.parser_creator import ParserCreator
from src.patterns.creational.factory.concrete_products.csv_parser import CsvParser
from src.patterns.creational.factory.product_interface.document_parser import DocumentParser

class CsvParserCreator(ParserCreator):
    def create_parser(self) -> DocumentParser:
        return CsvParser()
