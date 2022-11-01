from logging import INFO, DEBUG

from src.boards.board import Board
from src.evaluators.evaluator import Evaluator
import logging
logger = logging.getLogger(__name__)
log = logger.log


class BoardStateEvaluator(Evaluator):

    def evaluate(self, board: Board) -> int:
        score = 0
        if board.is_terminal_state():
            score = board.evaluate()

        # log(DEBUG, f"tic tac toe evaluator, score: {score}")
        return score
