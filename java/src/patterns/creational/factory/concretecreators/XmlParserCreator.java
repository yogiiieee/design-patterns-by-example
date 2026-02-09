package patterns.creational.factory.concretecreators;

import patterns.creational.factory.abstractcreator.ParserCreator;
import patterns.creational.factory.concreteproducts.XmlParser;
import patterns.creational.factory.productinterface.DocumentParser;

public class XmlParserCreator extends ParserCreator {
    @Override
    public DocumentParser createParser() {
        return new XmlParser();
    }
}
