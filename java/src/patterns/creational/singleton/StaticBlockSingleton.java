package patterns.creational.singleton;

class StaticBlockSingleton {
    // single static instance
    private static StaticBlockSingleton instance;

    // private constructor prevents object instantiation
    private StaticBlockSingleton() {
        // init logic here
    }

    // executed (only once) when the class is loaded
    static {
        try {
            instance = new StaticBlockSingleton();
        } catch (Exception e) {
            throw new RuntimeException("Error creating instance", e);
        }
    }

    public static StaticBlockSingleton getInstance() {
        return instance;
    }
}