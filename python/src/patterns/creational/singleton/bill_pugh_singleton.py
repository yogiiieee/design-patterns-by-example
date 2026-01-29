class BillPughSingleton:
    class _SingletonHelper:
        INSTANCE = None

    def __init__(self) -> None:
        # prevent multiple instantiation by raising an exception
        if BillPughSingleton._SingletonHelper.INSTANCE is not None:
            raise Exception("Cannot instantiate directly.")
        # init logic here

    @staticmethod
    def get_instance() -> "BillPughSingleton":
        return BillPughSingleton._SingletonHelper.INSTANCE
