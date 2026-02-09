from src.patterns.creational.factory.concrete_creators.csv_parser_creator import CsvParserCreator
from src.patterns.creational.factory.concrete_creators.json_parser_creator import JsonParserCreator
from src.patterns.creational.factory.concrete_creators.xml_parser_creator import XmlParserCreator

def main():
    csv_parser_creator = CsvParserCreator()
    json_parser_creator = JsonParserCreator()
    xml_parser_creator = XmlParserCreator()

    csv_parser_creator.parse("data.csv")
    json_parser_creator.parse("data.json")
    xml_parser_creator.parse("data.xml")

if __name__ == "__main__":
    main()

"""
Adding a new parser is simple:
Example:

class HtmlParser(DocumentParser):
    def parse(self, document: str) -> None:
        print(f"Parsing HTML document: {document}")

class HtmlParserCreator(ParserCreator):
    def create_parser(self) -> DocumentParser:
        return HtmlParser()

html_parser_creator = HtmlParserCreator()
html_parser_creator.parse("data.html")
"""
