from abc import abstractmethod

from src.evaluators.evaluator import Evaluator


class Expander:

    def __init__(self, evaluator: Evaluator):
        self.__evaluator = evaluator

    @property
    def evaluator(self):
        return self.__evaluator

    @abstractmethod
    def search(self, game, time_for_move=60):
        pass
