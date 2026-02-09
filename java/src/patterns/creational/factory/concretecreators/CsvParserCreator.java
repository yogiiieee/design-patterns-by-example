package patterns.creational.factory.concretecreators;

import patterns.creational.factory.abstractcreator.ParserCreator;
import patterns.creational.factory.concreteproducts.CsvParser;
import patterns.creational.factory.productinterface.DocumentParser;

public class CsvParserCreator extends ParserCreator {
    @Override
    public DocumentParser createParser() {
        return new CsvParser();
    }
}
