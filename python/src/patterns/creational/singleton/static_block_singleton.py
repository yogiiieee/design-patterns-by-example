class StaticBlockSingleton:
    _instance = None

    def __init__(self) -> None:
        # prevent multiple instantiation by raising an exception
        if StaticBlockSingleton._instance is not None:
            raise Exception("Cannot instantiate directly.")
        # init logic here

    @staticmethod
    def get_instance() -> "StaticBlockSingleton":
        return StaticBlockSingleton._instance

# instance created immediately on module import
try:
    StaticBlockSingleton._instance = StaticBlockSingleton()
except Exception as e:
    raise Exception("Error creating instance", e)
