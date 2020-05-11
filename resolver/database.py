class Database:
    __instance = None
    db = {'domains': {}}

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Database.__instance is None:
            Database()
        return Database.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Database.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Database.__instance = self