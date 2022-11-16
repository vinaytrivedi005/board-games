import time
from typing import List, Dict

from src.boards.board import Board
from src.players.player import Player
from logging import INFO
import logging
logger = logging.getLogger(__name__)
log = logger.log


class Game:

    def __init__(self, board: Board, players: List[Player], turn_order: List[Player]):
        self.__board = board
        self.__players = players
        self.__turn_order = turn_order
        self.__turn = turn_order[0]

    @property
    def players(self) -> List[Player]:
        return self.__players

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def turn(self) -> Player:
        return self.__turn

    @turn.setter
    def turn(self, turn: Player):
        self.__turn = turn

    @property
    def turn_order(self) -> List[Player]:
        return self.__turn_order

    def play(self, verbose = False):
        if verbose:
            print(self.board.get_pretty_board())
        while not self.board.is_terminal_state():
            start_time = time.time_ns()
            self.__move(self.turn)
            self._switch_turn()
            end_time = time.time_ns()
            if verbose:
                log(INFO, f"time_for_move: {int((end_time - start_time) / 1e9)}s")
                print(f"time_for_move: {int((end_time - start_time) / 1e9)}s")
                log(INFO, f"{self.board.get_pretty_board()}")
                print(self.board.get_pretty_board(), end="\n\n")

        return self.__board.evaluate()

    def __move(self, player: Player):
        move = player.move(self)
        log(INFO, "player: {} - move: {}".format(player.name, move))
        self.__board.insert(move)

    def _switch_turn(self):
        # TODO: temporary change to resolve defects
        # if self.turn == Properties.get(X):
        #     self.turn = Properties.get(O)
        # else:
        #     self.turn = Properties.get(X)

        next_turn_id = 0
        for i in range(len(self.turn_order)):  # turn_order: [O, X]
            if self.turn_order[i] == self.turn:  # turn = O
                next_turn_id = (i + 1) % len(self.turn_order)
                break
        self.turn = self.turn_order[next_turn_id]
