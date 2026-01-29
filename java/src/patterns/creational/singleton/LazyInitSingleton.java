package patterns.creational.singleton;

public class LazyInitSingleton {
    // single static instance
    private static LazyInitSingleton instance;

    // private constructor prevents object instantiation
    private LazyInitSingleton() {
        // init logic here
    }

    public static LazyInitSingleton getInstance() {
        // only create once (the first time this method is called)
        if (instance == null) {
            instance = new LazyInitSingleton();
        }
        return instance;
    }
}
