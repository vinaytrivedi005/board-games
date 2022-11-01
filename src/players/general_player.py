from src.players.player import Player
from src.players.timed_player import TimedPlayer


class GeneralPlayer(TimedPlayer):

    def __init__(self, expander, name="GeneralTimedPlayer"):
        super().__init__(name=name)
        self.__expander = expander

    def move(self, game, time_for_move=1):
        m = self.__expander.search(game, time_for_move)
        return m

    @property
    def expander(self):
        return self.__expander

    def is_pondering(self):
        return self.__expander.is_pondering
