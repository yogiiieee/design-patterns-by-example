package patterns.creational.factory.concreteproducts;

import patterns.creational.factory.productinterface.DocumentParser;

public class JsonParser implements DocumentParser {
    @Override
    public void parse(String document) {
        System.out.println("Parsing JSON document: " + document);
    }
}
