from src.expanders.random_expander import RandomExpander


class ExpanderFactory:
    __instance = None

    RANDOM_EXPANDER = "_ExpanderFactory__random_expander"

    def __init__(self):
        if ExpanderFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__expanders = {}

    @staticmethod
    def get_instance():
        if ExpanderFactory.__instance is None:
            ExpanderFactory.__instance = ExpanderFactory()

        return ExpanderFactory.__instance

    def get_expander(self, *args, **kwargs):
        if 'expander_id' not in kwargs.keys():
            return self.__default(*args, **kwargs)

        expander_id = kwargs.pop('expander_id')
        expander = getattr(self, expander_id, self.__default)
        return expander(*args, **kwargs)

    def __random_expander(self, *args, **kwargs):
        return RandomExpander(*args, **kwargs)

    def __default(self, *args, **kwargs):
        raise ValueError("No such expander exists.")
