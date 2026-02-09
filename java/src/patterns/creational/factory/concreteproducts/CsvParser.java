package patterns.creational.factory.concreteproducts;

import patterns.creational.factory.productinterface.DocumentParser;

public class CsvParser implements DocumentParser {
    @Override
    public void parse(String document) {
        System.out.println("Parsing CSV document: " + document);
    }
}
