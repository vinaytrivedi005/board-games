from src.boards.board import Board
from src.evaluators.evaluator import Evaluator
from src.games.game import Game
from src.players.random_player import RandomPlayer


class RandomSimulationEvaluator(Evaluator):

    def evaluate(self, board: Board):
        b = board.deep_copy()

        p1 = RandomPlayer()
        p2 = RandomPlayer()

        g = Game(b, [p1, p2], [p1, p2])
        return g.play()
