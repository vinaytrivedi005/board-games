import unittest

from src.boards.tic_tac_toe_board import TicTacToeBoard
from src.utilities.exceptions import InvalidMoveException

import numpy as np


class TicTacToeBoardTestCase(unittest.TestCase):
    def test_constructor1(self):
        expected_X = 0
        expected_O = 0

        tttb = TicTacToeBoard()
        actual_X = tttb.X
        actual_O = tttb.O

        self.assertEqual(expected_X, actual_X)
        self.assertEqual(expected_O, actual_O)

    def test_constructor2(self):
        expected_X = 4
        expected_O = 0

        tttb = TicTacToeBoard(X=4)
        actual_X = tttb.X
        actual_O = tttb.O

        self.assertEqual(expected_X, actual_X)
        self.assertEqual(expected_O, actual_O)

    def test_constructor3(self):
        expected_X = 6
        expected_O = 9

        tttb = TicTacToeBoard(X=6, O=9)
        actual_X = tttb.X
        actual_O = tttb.O

        self.assertEqual(expected_X, actual_X)
        self.assertEqual(expected_O, actual_O)

    def test_insert_x1(self):

        expected_X = 1

        tttb = TicTacToeBoard()
        tttb.insert('X', 'a1')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x2(self):

        expected_X = 2

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b1')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x3(self):

        expected_X = 4

        tttb = TicTacToeBoard()
        tttb.insert('X', 'c1')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x4(self):

        expected_X = 8

        tttb = TicTacToeBoard()
        tttb.insert('X', 'a2')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x5(self):

        expected_X = 16

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x6(self):

        expected_X = 32

        tttb = TicTacToeBoard()
        tttb.insert('X', 'c2')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x7(self):

        expected_X = 64

        tttb = TicTacToeBoard()
        tttb.insert('X', 'a3')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x8(self):

        expected_X = 128

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b3')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x9(self):

        expected_X = 256

        tttb = TicTacToeBoard()
        tttb.insert('X', 'c3')

        actual_X = tttb.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x_invalid_move1(self):

        with self.assertRaises(InvalidMoveException):

            tttb = TicTacToeBoard()
            tttb.insert('X', 'b2')
            tttb.insert('O', 'a1')
            tttb.insert('X', 'b2')

    def test_insert_x_invalid_move2(self):

        with self.assertRaises(InvalidMoveException):
            tttb = TicTacToeBoard()
            tttb.insert('X', 'b2')
            tttb.insert('O', 'a1')
            tttb.insert('X', 'a1')

    def test_insert_o1(self):

        expected_O = 1

        tttb = TicTacToeBoard()
        tttb.insert('O', 'a1')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o2(self):

        expected_O = 2

        tttb = TicTacToeBoard()
        tttb.insert('O', 'b1')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o3(self):

        expected_O = 4

        tttb = TicTacToeBoard()
        tttb.insert('O', 'c1')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o4(self):

        expected_O = 8

        tttb = TicTacToeBoard()
        tttb.insert('O', 'a2')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o5(self):

        expected_O = 16

        tttb = TicTacToeBoard()
        tttb.insert('O', 'b2')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o6(self):

        expected_O = 32

        tttb = TicTacToeBoard()
        tttb.insert('O', 'c2')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o7(self):

        expected_O = 64

        tttb = TicTacToeBoard()
        tttb.insert('O', 'a3')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o8(self):

        expected_O = 128

        tttb = TicTacToeBoard()
        tttb.insert('O', 'b3')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o9(self):

        expected_O = 256

        tttb = TicTacToeBoard()
        tttb.insert('O', 'c3')

        actual_O = tttb.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o_invalid_move1(self):

        with self.assertRaises(InvalidMoveException):

            tttb = TicTacToeBoard()
            tttb.insert('X', 'b2')
            tttb.insert('O', 'b2')

    def test_insert_o_invalid_move2(self):

        with self.assertRaises(InvalidMoveException):
            tttb = TicTacToeBoard()
            tttb.insert('X', 'b2')
            tttb.insert('O', 'a1')
            tttb.insert('X', 'c3')
            tttb.insert('O', 'a1')

    def test_evaluate_x_win1(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'a1')
        tttb.insert('X', 'b1')
        tttb.insert('X', 'c1')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win2(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'a2')
        tttb.insert('X', 'b2')
        tttb.insert('X', 'c2')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win3(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'a3')
        tttb.insert('X', 'b3')
        tttb.insert('X', 'c3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win4(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'a1')
        tttb.insert('X', 'a2')
        tttb.insert('X', 'a3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win5(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b1')
        tttb.insert('X', 'b2')
        tttb.insert('X', 'b3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win6(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'c1')
        tttb.insert('X', 'c2')
        tttb.insert('X', 'c3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win7(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'a1')
        tttb.insert('X', 'b2')
        tttb.insert('X', 'c3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win8(self):
        expected_result = 1
        tttb = TicTacToeBoard()
        tttb.insert('X', 'a3')
        tttb.insert('X', 'b2')
        tttb.insert('X', 'c1')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win1(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'a1')
        tttb.insert('O', 'b1')
        tttb.insert('O', 'c1')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win2(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'a2')
        tttb.insert('O', 'b2')
        tttb.insert('O', 'c2')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win3(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'a3')
        tttb.insert('O', 'b3')
        tttb.insert('O', 'c3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win4(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'a1')
        tttb.insert('O', 'a2')
        tttb.insert('O', 'a3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win5(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'b1')
        tttb.insert('O', 'b2')
        tttb.insert('O', 'b3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win6(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'c1')
        tttb.insert('O', 'c2')
        tttb.insert('O', 'c3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win7(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'a1')
        tttb.insert('O', 'b2')
        tttb.insert('O', 'c3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win8(self):
        expected_result = -1
        tttb = TicTacToeBoard()
        tttb.insert('O', 'a3')
        tttb.insert('O', 'b2')
        tttb.insert('O', 'c1')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_draw1(self):
        expected_result = 0
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        tttb.insert('X', 'c2')
        tttb.insert('O', 'a2')

        tttb.insert('X', 'a3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_in_progress1(self):
        expected_result = 2
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_in_progress2(self):
        expected_result = 2
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        tttb.insert('X', 'c2')

        actual_result = tttb.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_get_possible_moves1(self):
        expected_result = ['a2', 'a3']
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        tttb.insert('X', 'c2')

        actual_result = tttb.get_possible_moves()
        self.assertListEqual(sorted(expected_result), sorted(actual_result))

    def test_get_possible_moves2(self):
        expected_result = ['a2', 'a3', 'c2']
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        actual_result = tttb.get_possible_moves()
        self.assertListEqual(sorted(expected_result), sorted(actual_result))

    def test_is_valid_move1(self):
        expected_result = True
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        actual_result = tttb.is_valid_move('a2')
        self.assertEqual(expected_result, actual_result)

    def test_is_valid_move2(self):
        expected_result = False
        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        tttb.insert('X', 'c3')
        tttb.insert('O', 'c1')

        tttb.insert('X', 'b1')
        tttb.insert('O', 'b3')

        actual_result = tttb.is_valid_move('c1')
        self.assertEqual(expected_result, actual_result)

    def test_get_next_board_states1(self):
        expected_result = dict()

        for move in ['a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3']:
            tttb = TicTacToeBoard()
            tttb.insert('X', 'b2')
            tttb.insert('O', move)
            expected_result[move] = tttb

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')

        actual_result = tttb.get_next_board_states('O')

        for move, board in expected_result.items():
            self.assertIn(move, actual_result.keys())
            self.assertEqual(board, actual_result[move])

    def test_get_next_board_states2(self):
        expected_result = dict()

        for move in ['a1', 'b1', 'c1', 'a2', 'c2', 'b3', 'c3']:
            tttb = TicTacToeBoard()
            tttb.insert('X', 'b2')
            tttb.insert('O', 'a3')
            tttb.insert('X', move)
            expected_result[move] = tttb

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a3')

        actual_result = tttb.get_next_board_states('X')

        for move, board in expected_result.items():
            self.assertIn(move, actual_result.keys())
            self.assertEqual(board, actual_result[move])

    def test_deep_copy1(self):

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a3')

        tttb_copy = tttb.deep_copy()

        self.assertEqual(tttb, tttb_copy)

    def test_get_binary_board1(self):

        expected_bb = [[[0, 0], [0, 0], [0, 0]],
                       [[0, 0], [1, 0], [0, 0]],
                       [[0, 0], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')

        actual_bb = tttb.get_binary_board('X')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_binary_board2(self):

        expected_bb = [[[0, 0], [0, 0], [0, 0]],
                       [[0, 0], [0, 1], [0, 0]],
                       [[1, 0], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        actual_bb = tttb.get_binary_board('O')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_binary_board3(self):

        expected_bb = [[[0, 0], [0, 0], [1, 0]],
                       [[0, 0], [1, 0], [0, 0]],
                       [[0, 1], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')
        tttb.insert('X', 'c3')

        actual_bb = tttb.get_binary_board('X')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_binary_board4(self):

        expected_bb = [[[1, 0], [0, 0], [0, 1]],
                       [[0, 0], [0, 1], [0, 0]],
                       [[1, 0], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')
        tttb.insert('X', 'c3')
        tttb.insert('O', 'a3')

        actual_bb = tttb.get_binary_board('O')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_pretty_board1(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        expected_pb = pretty_board.format(*pieces)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')

        actual_pb = tttb.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)

    def test_get_pretty_board2(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = ['O', ' ', ' ', ' ', 'X', ' ', ' ',' ',' ']
        expected_pb = pretty_board.format(*pieces)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')

        actual_pb = tttb.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)

    def test_get_pretty_board3(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = ['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        expected_pb = pretty_board.format(*pieces)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')
        tttb.insert('X', 'c3')

        actual_pb = tttb.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)

    def test_get_pretty_board4(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = ['O', ' ', ' ', ' ', 'X', ' ', 'O', ' ', 'X']
        expected_pb = pretty_board.format(*pieces)

        tttb = TicTacToeBoard()
        tttb.insert('X', 'b2')
        tttb.insert('O', 'a1')
        tttb.insert('X', 'c3')
        tttb.insert('O', 'a3')

        actual_pb = tttb.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)


if __name__ == '__main__':
    unittest.main()
