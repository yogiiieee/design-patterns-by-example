package patterns.creational.singleton;

class DoubleCheckLockSingleton {
    // single static instance
    // volatile keyword for immediate visibility of changes to all threads
    private static volatile DoubleCheckLockSingleton instance;

    // private constructor prevents object instantiation
    private DoubleCheckLockSingleton() {
        // init logic here
    }

    public static DoubleCheckLockSingleton getInstance() {
        // only create once (the first time this method is called)
        // first check -> not synchronized
        if (instance == null) {
            // thread lock to allow one thread at a time
            synchronized (DoubleCheckLockSingleton.class) {
                // double check -> synchronized
                if (instance == null) {
                    instance = new DoubleCheckLockSingleton();
                }
            }
        }
        return instance;
    }
}
