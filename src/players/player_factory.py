from src.players.random_player import RandomPlayer
from src.players.human_player import HumanPlayer
from src.players.general_player import GeneralPlayer
from src.players.minimax_player import MiniMaxPlayer
from src.players.mcts_player import MCTSPlayer


class PlayerFactory:
    __instance = None

    RANDOM_PLAYER = "_PlayerFactory__random_player"
    MINIMAX_PLAYER = "_PlayerFactory__minimax_player"
    GENERAL_PLAYER = "_PlayerFactory__general_player"
    HUMAN_PLAYER = "_PlayerFactory__human_player"
    MCTS_PLAYER = "_PlayerFactory__mcts_player"

    def __init__(self):
        if PlayerFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__players = {}

    @staticmethod
    def get_instance():
        if PlayerFactory.__instance is None:
            PlayerFactory.__instance = PlayerFactory()

        return PlayerFactory.__instance

    def get_player(self, *args, **kwargs):
        if 'player_id' not in kwargs.keys():
            return self.__default(*args, **kwargs)

        player_id = kwargs.pop('player_id')
        player = getattr(self, player_id, self.__default)
        return player(*args, **kwargs)

    def __random_player(self, *args, **kwargs):
        return RandomPlayer(*args, **kwargs)

    def __human_player(self, *args, **kargs):
        return HumanPlayer(*args, *kargs)

    def __general_player(self, *args, **kargs):
        return GeneralPlayer(*args, *kargs)

    def __minimax_player(self, *args, **kargs):
        return MiniMaxPlayer(*args, *kargs)

    def __mcts_player(self, *args, **kargs):
        return MCTSPlayer(*args, *kargs)

    def __default(self, *args, **kwargs):
        raise ValueError("No such expander exists.")
