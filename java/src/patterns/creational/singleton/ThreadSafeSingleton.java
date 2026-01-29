package patterns.creational.singleton;

class ThreadSafeSingleton {
    // single static instance
    private static ThreadSafeSingleton instance;

    // private constructor prevents object instantiation
    private ThreadSafeSingleton() {
        // init logic here
    }

    // synchronized keyword to allow one thread at a time
    public static synchronized ThreadSafeSingleton getInstance() {
        // only create once (the first time this method is called)
        if (instance == null) {
            instance = new ThreadSafeSingleton();
        }
        return instance;
    }
}
