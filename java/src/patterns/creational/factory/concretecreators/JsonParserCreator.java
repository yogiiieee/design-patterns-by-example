package patterns.creational.factory.concretecreators;

import patterns.creational.factory.abstractcreator.ParserCreator;
import patterns.creational.factory.concreteproducts.JsonParser;
import patterns.creational.factory.productinterface.DocumentParser;

public class JsonParserCreator extends ParserCreator {
    @Override
    public DocumentParser createParser() {
        return new JsonParser();
    }
}
