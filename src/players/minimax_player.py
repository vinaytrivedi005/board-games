import logging
import math
from logging import DEBUG, INFO

from src.games.game import Game
from src.players.player import Player
from src.utilities.constants import *
from src.utilities.properties import Properties

logger = logging.getLogger(__name__)
log = logger.log


class MiniMaxPlayer(Player):

    def __init__(self, name: str = "MiniMaxPlayer"):
        super().__init__(name=name)

    def move(self, game: Game):
        best_score = -math.inf
        best_move = None

        possible_moves = game.board.get_possible_moves()

        for move in possible_moves:
            temp_board = game.board.deep_copy()
            log(INFO, "initial position: \n {}".format(temp_board.get_pretty_board()))
            turn = temp_board.turn
            log(INFO, "game turn: {}".format(turn))
            maximizer_mark = turn
            temp_board.insert(move)
            turn = self.__switch_turn(turn)
            score = self._minimax(False, maximizer_mark, temp_board, turn, 1)
            log(INFO, "move: {} - score: {} - depth: {}".format(move, score, 1))
            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(self, maximizing, maximizer_mark, board, turn, depth=0):
        if board.is_terminal_state():
            result = self.__evaluate(board, maximizer_mark, depth)
            log(DEBUG, "maximizing: {} - maximizer_mark: {} - turn: {} - depth: {} - result: {}".format(maximizing, maximizer_mark, turn, depth + 1, result))
            return result

        scores = list()
        possible_moves = board.get_possible_moves()

        for move in possible_moves:
            temp_board = board.deep_copy()
            temp_board.insert(move)
            switched_turn = self.__switch_turn(turn)
            score = self._minimax(not maximizing, maximizer_mark, temp_board, switched_turn, depth + 1)
            log(DEBUG, "turn: {} - move: {} - score: {} - depth: {}".format(turn, move, score, depth + 1))
            scores.append(score)

        log(DEBUG, f"maximizing: {maximizing} - scores: {scores}")
        log(DEBUG, f"{board.get_pretty_board()}")

        return max(scores) if maximizing else min(scores)

    def __switch_turn(self, turn):
        return Properties.get(O) if turn == Properties.get(X) else Properties.get(X)

    def __evaluate(self, board, maximizer_mark, depth):
        # TODO: write a generalized code for any game like below commented code for tic tac toe
        score = board.evaluate()
        pieces = board.pieces
        if score == 0:
            return score
        score = score * 10
        if score > 0:
            score = score - depth
        else:
            score = score + depth
        if maximizer_mark == pieces[0]:
            return score
        if maximizer_mark == pieces[1]:
            return -score
