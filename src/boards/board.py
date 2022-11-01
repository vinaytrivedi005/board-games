from abc import abstractmethod
from typing import List


class Board:

    def __init__(self, pieces: list, board_name="Board"):
        self.__board_name = board_name
        self.__pieces = pieces

    @property
    def board_name(self):
        return self.__board_name

    @property
    def pieces(self):
        return self.__pieces

    @abstractmethod
    def insert(self, move: str) -> None:
        pass

    @abstractmethod
    def evaluate(self) -> int:
        pass

    @abstractmethod
    def is_terminal_state(self) -> int:
        pass

    @abstractmethod
    def get_possible_moves(self) -> List[str]:
        pass
