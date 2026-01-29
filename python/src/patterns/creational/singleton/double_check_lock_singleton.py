import threading


class DoubleCheckLockSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        # prevent multiple instantiation by raising an exception
        if DoubleCheckLockSingleton._instance is not None:
            raise Exception("Cannot instantiate directly.")
        # init logic here

    @staticmethod
    def get_instance() -> "DoubleCheckLockSingleton":
        # only create once (the first time this method is called)
        # first check -> not synchronized
        if DoubleCheckLockSingleton._instance is None:
            # thread lock to allow one thread at a time
            with DoubleCheckLockSingleton._lock:
                # double check -> synchronized
                if DoubleCheckLockSingleton._instance is None:
                    DoubleCheckLockSingleton._instance = DoubleCheckLockSingleton()
        return DoubleCheckLockSingleton._instance
