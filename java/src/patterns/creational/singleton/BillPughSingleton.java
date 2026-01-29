package patterns.creational.singleton;

class BillPughSingleton {
    // private constructor prevents object instantiation
    private BillPughSingleton() {
        // init logic here
    }

    // static class to hold the single instance
    private static class SingletonHelper {
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }

    public static BillPughSingleton getInstance() {
        return SingletonHelper.INSTANCE;
    }
}
