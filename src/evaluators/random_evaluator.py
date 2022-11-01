import random

from src.boards.board import Board
from src.evaluators.evaluator import Evaluator


class RandomEvaluator(Evaluator):

    def evaluate(self, board: Board):
        score = random.uniform(-1.0, 1.0)
        return score
