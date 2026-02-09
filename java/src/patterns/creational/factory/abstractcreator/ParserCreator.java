package patterns.creational.factory.abstractcreator;

import patterns.creational.factory.productinterface.DocumentParser;

public abstract class ParserCreator {
    public abstract DocumentParser createParser();

    public void parse(String document) {
        DocumentParser parser = createParser();
        parser.parse(document);
    }
}
