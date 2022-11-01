import numpy as np

from src.boards.board import Board
from src.utilities.constants import *
from src.utilities.properties import Properties
from src.utilities.exceptions import InvalidMoveException


class TicTacToeBoard(Board):
    """
    This class is designed to implement API to manipulate tic tac toe board.
    We will always mark board with the perspective of X, marking files(columns) as a, b, c from left to right and
    ranks(rows) as 1, 2, 3 from bottom to top.
    3 __|__|__
    2 __|__|__
    1   |  |
      a  b  c
    Thus, each square will be represented by a letter followed by a number, i.e. a1, b3, c2 etc.
    The board will be described using two integers for X and O.
    The last 9 bits of integer will each hold the value for presence of particular piece, i.e. if X is present at
    a3 then 7th bit will have 1 in int X.

    """

    def __init__(self, X: int = 0, O: int = 0, turn_order=[], board_name="TicTacToeBoard"):
        """
        initializes tic tac toe board with given squares of Xs by X and Os by O. default 0, 0.
        :param X:
        :param O:
        """
        super().__init__(pieces=Properties.get(TTT_PIECES), board_name="TicTacToeBoard")
        self.__X = X
        self.__O = O
        self.__turn_order = turn_order if turn_order else self.pieces
        self.__turn = self.__turn_order[0]
        self.__board_length = Properties.get(TTT_LENGTH)
        self.__board_width = Properties.get(TTT_WIDTH)
        self.__moves = list()
        self.__result = None

    @property
    def X(self):
        return self.__X

    @property
    def O(self):
        return self.__O

    @property
    def board_length(self):
        return self.__board_length

    @property
    def board_width(self):
        return self.__board_width

    @property
    def turn(self):
        return self.__turn

    @property
    def moves(self):
        return self.__moves

    @property
    def result(self):
        if self.__result is None:
            self.__result = self.evaluate() if self.is_terminal_state() else None

        return self.__result

    @result.setter
    def result(self, result):
        self.__result = result

    def insert(self, move: str) -> None:
        """
        will insert 1 int the integer representing the piece at given square.
        For example: piece = 'X', position 'c2' then we will add 2^5 in X.
        :param move: any valid move from a1 to c3
        :return: None
        :raises: InvalidMoveException: if square is already filled.
        """
        if not self.is_valid_move(move):
            raise InvalidMoveException("invalid move: {}".format(move), dict())

        if self.__turn == Properties.get(X):
            self.__insert_x(move)
        if self.__turn == Properties.get(O):
            self.__insert_o(move)

        self.__moves.append(move)
        self.__switch_turn()

    def __insert_x(self, square):
        power = self.__convert(square=square)
        self.__X += 2 ** power

    def __insert_o(self, square):
        power = self.__convert(square=square)
        self.__O += 2 ** power

    def evaluate(self) -> int:
        """
        Evaluate the board position weather it is win for X, O, Draw or InProgress.
        :return: 0=Draw, 1=X win, -1=O win, 2=InProgress
        """
        if self.__result is not None:
            return self.__result
        if self.__evaluate_win_x():
            return Properties.get(GAME_STATES).get(GAME_STATES_WIN_X)
        if self.__evaluate_win_o():
            return Properties.get(GAME_STATES).get(GAME_STATES_WIN_O)
        if self.__evaluate_draw():
            return Properties.get(GAME_STATES).get(GAME_STATES_DRAW)
        return Properties.get(GAME_STATES).get(GAME_STATES_IN_PROGRESS)

    def __evaluate_win_x(self):
        winning_positions = Properties.get(WINNING_POSITIONS)

        for winning_position in winning_positions:
            if self.X & winning_position == winning_position:
                return True

        return False

    def __evaluate_win_o(self):
        winning_positions = Properties.get(WINNING_POSITIONS)

        for winning_position in winning_positions:
            if self.O & winning_position == winning_position:
                return True

        return False

    def __evaluate_draw(self):
        return (self.X | self.O) == 511

    def get_pretty_board(self):
        """
        Generate a string representation of board which looks like actual tic tac toe board. i.e.

        X | O |
        --|---|---
        O | X | X
        --|---|--
          | X | O

        :return str: string of the board containing Xs and Os
        """
        pretty_pieces = []
        and_op = 1

        board_size = self.board_length * self.board_width
        for count in range(0, board_size):
            if self.X & and_op != 0:
                pretty_pieces.append(Properties.get(X))
            elif self.O & and_op != 0:
                pretty_pieces.append(Properties.get(O))
            else:
                pretty_pieces.append(' ')
            and_op = and_op << 1

        pretty_board = Properties.get(TTT_PRETTY_BOARD)
        pretty_board = pretty_board.format(*pretty_pieces)

        return pretty_board

    def get_binary_board(self, piece):
        """
        Generate a numpy 2 dimensional array with 1s and 0s representing board as binary with the perspective of piece.
        X | O |
        --|---|---
        O | X | X
        --|---|--
          | X | O

        the equivalent binary representation for above board with the perspective of X is as follows:
        [[[1 0], [0 1], [0 0]],
         [[0 1], [1 0], [1 0]],
         [[0 0], [1 0], [0 1]]]

        the equivalent binary representation for above board with the perspective of X is as follows:
        [[[0 1], [1 0], [0 0]],
         [[1 0], [0 1], [0 1]],
         [[0 0], [0 1], [1 0]]]

        :param piece: 'X' or 'O'
        :return numpy array: 3x3x2 representation for binary board
        """
        binary_board = []
        row = []
        and_op = 1

        board_size = self.board_length * self.board_width
        for count in range(0, board_size):

            piece_X = 1 if self.X & and_op else 0
            piece_O = 1 if self.O & and_op else 0
            if piece == Properties.get(X):
                row.append([piece_X, piece_O])
            elif piece == Properties.get(O):
                row.append([piece_O, piece_X])
            and_op = and_op << 1

            #   since count starts from 0, i have used count+1 in below condition.
            if (count + 1) % self.board_length == 0:
                binary_board.insert(0, row)
                row = []

        return np.array(binary_board)

    def get_possible_moves(self):
        """
        return the list of empty squares on the board
        :return list: possible moves
        """

        if self.is_terminal_state():
            return list()

        moves = list()
        and_op = 1

        board_size = self.board_length * self.board_width
        for count in range(0, board_size):
            piece_X = 1 if self.X & and_op else 0
            piece_O = 1 if self.O & and_op else 0
            if piece_X == 0 and piece_O == 0:
                moves.append(self.__convert_index_to_square(count))
            and_op = and_op << 1

        return moves

    def deep_copy(self):
        """
        deep copy the board

        :return:
        """
        turn_order_len = len(self.__turn_order)
        turn_order = [t for t in self.__turn_order]

        if self.__turn != turn_order[0]:
            turn_order = turn_order[::-1]

        tttb = TicTacToeBoard(self.X, self.O, turn_order)

        return tttb

    def get_next_board_states(self, piece):
        """
        return all possible states of the board after inserting the piece.

        :param piece: 'X' or 'O'
        :return:
        """
        possible_moves = self.get_possible_moves()

        board_states = dict()
        for move in possible_moves:
            tttb = self.deep_copy()
            tttb.insert(move)
            board_states[move] = tttb

        return board_states

    def is_valid_move(self, square):
        """
        validate the move on a particular square:

        :param square:
        :return:
        """
        if self.is_terminal_state():
            return False

        power = self.__convert(square=square)
        if power is None or power not in range(0, 9):
            return False

        if self.X & 2 ** power != 0 or self.O & 2 ** power != 0:
            return False

        return True

    def __convert(self, square=None, index=None):
        """
        convert from square to index and index to square based on argument. i.e
        a1 -> 1
        3 -> c1
        6 -> c2
        b3 -> 8

        :param square:
        :param index:
        :return:
        """
        if square is not None:
            return self.__convert_square_to_index(square)
        if index is not None:
            return self.__convert_index_to_square(index)

    def __convert_square_to_index(self, square):
        return Properties.get(TTT_SQUARE_TO_INDEX).get(square)

    def __convert_index_to_square(self, index):
        return Properties.get(TTT_INDEX_TO_SQUARE).get(str(index))

    def __eq__(self, other):
        if self.X != other.X:
            return False

        if self.O != other.O:
            return False

        if self.turn != other.turn:
            return False

        if self.board_name != other.board_name:
            return False

        return True

    def __switch_turn(self):
        # TODO: temporary change to resolve defects
        # if self.turn == Properties.get(X):
        #     self.turn = Properties.get(O)
        # else:
        #     self.turn = Properties.get(X)

        next_turn_id = 0
        for i in range(len(self.__turn_order)):  # turn_order: [O, X]
            if self.__turn_order[i] == self.__turn:  # turn = O
                next_turn_id = (i + 1) % len(self.__turn_order)
                break
        self.__turn = self.__turn_order[next_turn_id]

    def is_terminal_state(self):
        return True if self.evaluate() != Properties.get(GAME_STATES).get(GAME_STATES_IN_PROGRESS) else False

    def __str__(self):
        board = f"TicTacToeBoard: (X: {self.X:b}, O: {self.O:b}, turn: {self.turn}, turn_order: {self.__turn_order})"
        return board

    def __repr__(self):
        board = f"TicTacToeBoard: (X: {self.X:b}, O: {self.O:b}, turn: {self.turn}, turn_order: {self.__turn_order})"
        return board

