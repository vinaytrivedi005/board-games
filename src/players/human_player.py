import time

from src.games.game import Game
from src.players.timed_player import TimedPlayer


class HumanPlayer(TimedPlayer):

    def __init__(self, name: str = "HumanPlayer"):
        super().__init__(name=name)
        self.__pondering = False

    def move(self, game: Game, time_for_move=1):
        self.__pondering = True
        pc = game.get_clock(self)
        possible_moves = game.board.get_possible_moves()
        move = ""
        while move not in possible_moves:
            if pc.is_stop_time():
                break
            print(f'You have {pc.time_for_move() // 1e9} seconds to move.')
            move = input(f"please enter your move out of possible moves {possible_moves}: ")
        self.__pondering = False
        return move

    def is_pondering(self):
        return self.__pondering
