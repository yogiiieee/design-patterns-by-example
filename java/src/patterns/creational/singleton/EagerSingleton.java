package patterns.creational.singleton;

class EagerSingleton {
    // single static instance instantiated eagerly
    private static final EagerSingleton instance = new EagerSingleton();

    // private constructor prevents object instantiation
    private EagerSingleton() {
        // init logic here
    }

    public static EagerSingleton getInstance() {
        return instance;
    }
}
