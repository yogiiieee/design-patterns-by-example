class EagerSingleton:
    _instance = None

    def __init__(self) -> None:
        # prevent multiple instantiation by raising an exception
        if EagerSingleton._instance is not None:
            raise Exception("Cannot instantiate directly.")
        # init logic here

    @staticmethod
    def get_instance() -> "EagerSingleton":
        return EagerSingleton._instance

# create instance immediately on module import
EagerSingleton._instance = EagerSingleton()
