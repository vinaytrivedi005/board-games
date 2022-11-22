import random

from src.evaluators.evaluator import Evaluator
from src.expanders.expander import Expander


class EvaluatorBasedExpander(Expander):

    def __init__(self, evaluator: Evaluator):
        super().__init__(evaluator)
        self.is_pondering = False

    def search(self, game, time_for_move=60):
        while True:
            board = game.board
            scores = self.__calculate_scores(board)
            scores.sort(key=lambda x: x[1], reverse=True if game.turn == game.players[0] else False)
            return scores[0][0]

    def __calculate_scores(self, board):
        possible_moves = board.get_possible_moves()
        scores = list()
        for move in possible_moves:
            temp_board = board.deep_copy()
            temp_board.insert(move)
            score = self.evaluator.evaluate(temp_board)
            scores.append((move, score))

        return scores
