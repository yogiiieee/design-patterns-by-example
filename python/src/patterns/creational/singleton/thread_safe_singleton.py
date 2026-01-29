import threading


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        # prevent multiple instantiation by raising an exception
        if ThreadSafeSingleton._instance is not None:
            raise Exception("Cannot instantiate directly.")
        # init logic here

    @staticmethod
    def get_instance() -> "ThreadSafeSingleton":
        # only create once (the first time this method is called)
        # thread lock to allow one thread at a time
        with ThreadSafeSingleton._lock:
            if ThreadSafeSingleton._instance is None:
                ThreadSafeSingleton._instance = ThreadSafeSingleton()
        return ThreadSafeSingleton._instance
