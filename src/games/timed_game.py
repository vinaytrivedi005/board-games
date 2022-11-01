import math
import time
from logging import INFO, DEBUG, ERROR
from typing import List, Dict

from src.boards.board import Board
from src.clocks.clock import Clock
from src.games.game import Game
from src.players.timed_player import TimedPlayer
from src.utilities.constants import GAME_STATES, GAME_STATES_IN_PROGRESS
from src.utilities.exceptions import TimeoutException
from src.utilities.properties import Properties
import logging
logger = logging.getLogger(__name__)
log = logger.log


class TimedGame(Game):

    def __init__(self, board: Board, players: List[TimedPlayer], turn_order: List[TimedPlayer], clocks: Dict[TimedPlayer, Clock]):
        super().__init__(board, players, turn_order)
        self.__clocks = clocks

    # @property
    # def players(self) -> List[TimedPlayer]:
    #     return super().players
    #
    # @property
    # def board(self) -> Board:
    #     return super().board
    #
    # @property
    # def turn(self) -> TimedPlayer:
    #     return super().turn
    #
    # @turn.setter
    # def turn(self, turn: TimedPlayer):
    #     super().turn = turn
    #
    # @property
    # def turn_order(self) -> List[TimedPlayer]:
    #     return super().turn_order

    @property
    def clocks(self):
        return self.__clocks

    def get_clock(self, player: TimedPlayer):
        return self.__clocks[player]

    def play(self, verbose=False):
        if verbose:
            print(self.board.get_pretty_board())
        log(DEBUG, "{}\n\n".format(self.board.get_pretty_board()))
        while self.board.evaluate() == Properties.get(GAME_STATES).get(GAME_STATES_IN_PROGRESS):
            start_time = time.time_ns()

            self.__clocks[self.turn].start()
            try:
                self.__move(self.turn)
            except TimeoutException as te:
                # TODO: need to add the code to give the winner in case of timeout, also for multiplayer game need to
                #  decide how to continue the game with other players
                log(ERROR, f"timeout for player: {self.turn}")
                break
            self.__clocks[self.turn].stop()
            self._switch_turn()
            log(DEBUG, "{}\n\n".format(self.board.get_pretty_board()))
            end_time = time.time_ns()
            if verbose:
                log(INFO, f"time_for_move: {int((end_time - start_time) / 1e9)}s")
                print(f"time_for_move: {int((end_time - start_time) / 1e9)}s")
                log(INFO, f"{self.board.get_pretty_board()}")
                print(self.board.get_pretty_board(), end="\n\n")
        result = self.board.evaluate()
        log(INFO, "result: {}".format(result))
        return result

    def __move(self, player: TimedPlayer):
        move = None
        clock = self.__clocks[player]
        time_for_move = clock.time_for_move()
        it = 0

        while not clock.is_stop_time():
            log(DEBUG, f"player: {player}, move iteration:{it}")
            move = player.move(self, time_for_move)
            # TODO: decide a way to get flag to not wait for better move from player
            if not player.is_pondering():
                break
            it += 1
        if move is None:
            raise TimeoutException("timeout for player: {}".format(player))
        log(INFO, "player: {} - move: {}".format(player.name, move))
        self.board.insert(move)
