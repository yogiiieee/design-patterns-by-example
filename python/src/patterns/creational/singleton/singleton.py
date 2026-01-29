class LazyInitSingleton:
    _instance = None

    def __init__(self) -> None:
        # prevent multiple instantiation by raising an exception
        if LazyInitSingleton._instance is not None:
            raise Exception("Cannot instantiate directly.")
        # init logic here

    @staticmethod
    def get_instance() -> "LazyInitSingleton":
        # only create once (the first time this method is called)
        if LazyInitSingleton._instance is None:
            LazyInitSingleton._instance = LazyInitSingleton()
        return LazyInitSingleton._instance
