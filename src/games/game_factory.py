from src.games.game import Game
from src.games.timed_game import TimedGame


class GameFactory:
    __instance = None

    UNTIMED_GAME = "_GameFactory__untimed_game"
    TIMED_GAME = "_GameFactory__timed_game"

    def __init__(self):
        if GameFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__games = {}

    @staticmethod
    def get_instance():
        if GameFactory.__instance is None:
            GameFactory.__instance = GameFactory()

        return GameFactory.__instance

    def get_game(self, *args, **kwargs):
        if 'game_id' not in kwargs.keys():
            return self.__default(*args, **kwargs)

        game_id = kwargs.pop('game_id')
        game = getattr(self, game_id, self.__default)
        return game(*args, **kwargs)

    def __untimed_game(self, *args, **kwargs):
        return Game(*args, **kwargs)

    def __timed_game(self, *args, **kwargs):
        return TimedGame(*args, **kwargs)

    def __default(self, *args, **kwargs):
        raise ValueError("No such game exists.")
