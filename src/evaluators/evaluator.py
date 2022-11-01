from abc import abstractmethod

from src.boards.board import Board


class Evaluator:

    @abstractmethod
    def evaluate(self, board: Board) -> int:
        """
        This function evaluates the board position and returns a score s where s belongs to [-1, 1]

        example:
            suppose for the game of chess the evaluation function is based on material count,
            if score of a pawn, sp = 1
            if score of a knight, sn = 3
            if score of a bishop, sb = 3
            if score of a rook, sr = 5
            if score of a queen, sq = 9

            maximum possible score of the board, max_score = 9*sq + 2*sn + 2*sb + 2*sr = 81 + 6 + 6 + 10 = 103

            if white has a queen and 2 pawn on the board and black has 2 rooks on the board then

            board_score = (white_score - black_score) / max_score

            board_score = (1*9 + 2*1 - 2*5) / 103 = 2/103 = 0.02

        :param board: board to be evaluated
        :return score int: an integer between -1 and 1 as evaluation score of board position.
        """
        pass
