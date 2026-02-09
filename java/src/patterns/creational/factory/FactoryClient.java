package patterns.creational.factory;

import patterns.creational.factory.abstractcreator.ParserCreator;
import patterns.creational.factory.concretecreators.CsvParserCreator;
import patterns.creational.factory.concretecreators.JsonParserCreator;
import patterns.creational.factory.concretecreators.XmlParserCreator;

public class FactoryClient {
    public static void main(String[] args) {
        ParserCreator creator;

        creator = new CsvParserCreator();
        creator.parse("data.csv");

        creator = new JsonParserCreator();
        creator.parse("data.json");

        creator = new XmlParserCreator();
        creator.parse("data.xml");
    }
}

/*
Adding a new parser is simple:
Example:

class HtmlParser implements DocumentParser {
    @Override
    public void parse(String document) {
        System.out.println("Parsing HTML document: " + document);
    }
}

class HtmlParserCreator extends ParserCreator {
    @Override
    public DocumentParser createParser() {
        return new HtmlParser();
    }
}

creator = new HtmlParserCreator();
creator.parse("data.html");

*/
