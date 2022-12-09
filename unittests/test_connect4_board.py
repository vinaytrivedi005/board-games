import unittest

from src.boards.connect4_board import Connect4Board
from src.utilities.exceptions import InvalidMoveException

import numpy as np


class Connect4BoardTestCase(unittest.TestCase):
    def test_constructor1(self):
        expected_X = 0
        expected_O = 0

        connect4b = Connect4Board()
        actual_X = connect4b.X
        actual_O = connect4b.O

        self.assertEqual(expected_X, actual_X)
        self.assertEqual(expected_O, actual_O)

    def test_constructor2(self):
        expected_X = 4
        expected_O = 0

        connect4b = Connect4Board(X=4)
        actual_X = connect4b.X
        actual_O = connect4b.O

        self.assertEqual(expected_X, actual_X)
        self.assertEqual(expected_O, actual_O)

    def test_constructor3(self):
        expected_X = 6
        expected_O = 9

        connect4b = Connect4Board(X=6, O=9)
        actual_X = connect4b.X
        actual_O = connect4b.O

        self.assertEqual(expected_X, actual_X)
        self.assertEqual(expected_O, actual_O)

    def test_insert_x1(self):

        expected_X = 1

        connect4b = Connect4Board()
        connect4b.insert('X', 'a1')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x2(self):

        expected_X = 2

        connect4b = Connect4Board()
        connect4b.insert('X', 'b1')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x3(self):

        expected_X = 4

        connect4b = Connect4Board()
        connect4b.insert('X', 'c1')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x4(self):

        expected_X = 8

        connect4b = Connect4Board(X=1, O=2)
        connect4b.insert('X', 'a2')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x5(self):

        expected_X = 16

        connect4b = Connect4Board(X=1, O=2)
        connect4b.insert('X', 'b2')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x6(self):

        expected_X = 32

        connect4b = Connect4Board(X=4, O=2)
        connect4b.insert('X', 'c2')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x7(self):

        expected_X = 64

        connect4b = Connect4Board(X=1, O=128)
        connect4b.insert('X', 'a3')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x8(self):

        expected_X = 128

        connect4b = Connect4Board(X=2, O=256)
        connect4b.insert('X', 'b3')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x9(self):

        expected_X = 256

        connect4b = Connect4Board(X=2, O=512)
        connect4b.insert('X', 'c3')

        actual_X = connect4b.X
        self.assertEqual(expected_X, actual_X)

    def test_insert_x_invalid_move1(self):

        with self.assertRaises(InvalidMoveException):

            connect4b = Connect4Board()
            connect4b.insert('X', 'a1')
            connect4b.insert('O', 'a2')
            connect4b.insert('X', 'a2')

    def test_insert_x_invalid_move2(self):

        with self.assertRaises(InvalidMoveException):
            connect4b = Connect4Board()
            connect4b.insert('X', 'a1')
            connect4b.insert('O', 'a2')
            connect4b.insert('X', 'a1')

    def test_insert_x_invalid_move3(self):

        with self.assertRaises(InvalidMoveException):
            connect4b = Connect4Board()
            connect4b.insert('X', 'a1')
            connect4b.insert('O', 'b1')
            connect4b.insert('X', 'a5')

    # TODO: Edit tests from here
    def test_insert_o1(self):

        expected_O = 1

        connect4b = Connect4Board()
        connect4b.insert('O', 'a1')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o2(self):

        expected_O = 2

        connect4b = Connect4Board()
        connect4b.insert('O', 'b1')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o3(self):

        expected_O = 4

        connect4b = Connect4Board()
        connect4b.insert('O', 'c1')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o4(self):

        expected_O = 8

        connect4b = Connect4Board()
        connect4b.insert('O', 'a2')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o5(self):

        expected_O = 16

        connect4b = Connect4Board()
        connect4b.insert('O', 'b2')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o6(self):

        expected_O = 32

        connect4b = Connect4Board()
        connect4b.insert('O', 'c2')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o7(self):

        expected_O = 64

        connect4b = Connect4Board()
        connect4b.insert('O', 'a3')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o8(self):

        expected_O = 128

        connect4b = Connect4Board()
        connect4b.insert('O', 'b3')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o9(self):

        expected_O = 256

        connect4b = Connect4Board()
        connect4b.insert('O', 'c3')

        actual_O = connect4b.O
        self.assertEqual(expected_O, actual_O)

    def test_insert_o_invalid_move1(self):

        with self.assertRaises(InvalidMoveException):

            connect4b = Connect4Board()
            connect4b.insert('X', 'b2')
            connect4b.insert('O', 'b2')

    def test_insert_o_invalid_move2(self):

        with self.assertRaises(InvalidMoveException):
            connect4b = Connect4Board()
            connect4b.insert('X', 'b2')
            connect4b.insert('O', 'a1')
            connect4b.insert('X', 'c3')
            connect4b.insert('O', 'a1')

    def test_evaluate_x_win1(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'a1')
        connect4b.insert('X', 'b1')
        connect4b.insert('X', 'c1')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win2(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'a2')
        connect4b.insert('X', 'b2')
        connect4b.insert('X', 'c2')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win3(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'a3')
        connect4b.insert('X', 'b3')
        connect4b.insert('X', 'c3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win4(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'a1')
        connect4b.insert('X', 'a2')
        connect4b.insert('X', 'a3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win5(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'b1')
        connect4b.insert('X', 'b2')
        connect4b.insert('X', 'b3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win6(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'c1')
        connect4b.insert('X', 'c2')
        connect4b.insert('X', 'c3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win7(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'a1')
        connect4b.insert('X', 'b2')
        connect4b.insert('X', 'c3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_x_win8(self):
        expected_result = 1
        connect4b = Connect4Board()
        connect4b.insert('X', 'a3')
        connect4b.insert('X', 'b2')
        connect4b.insert('X', 'c1')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win1(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'a1')
        connect4b.insert('O', 'b1')
        connect4b.insert('O', 'c1')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win2(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'a2')
        connect4b.insert('O', 'b2')
        connect4b.insert('O', 'c2')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win3(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'a3')
        connect4b.insert('O', 'b3')
        connect4b.insert('O', 'c3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win4(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'a1')
        connect4b.insert('O', 'a2')
        connect4b.insert('O', 'a3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win5(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'b1')
        connect4b.insert('O', 'b2')
        connect4b.insert('O', 'b3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win6(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'c1')
        connect4b.insert('O', 'c2')
        connect4b.insert('O', 'c3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win7(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'a1')
        connect4b.insert('O', 'b2')
        connect4b.insert('O', 'c3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_o_win8(self):
        expected_result = -1
        connect4b = Connect4Board()
        connect4b.insert('O', 'a3')
        connect4b.insert('O', 'b2')
        connect4b.insert('O', 'c1')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_draw1(self):
        expected_result = 0
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        connect4b.insert('X', 'c2')
        connect4b.insert('O', 'a2')

        connect4b.insert('X', 'a3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_in_progress1(self):
        expected_result = 2
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_evaluate_in_progress2(self):
        expected_result = 2
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        connect4b.insert('X', 'c2')

        actual_result = connect4b.evaluate()
        self.assertEqual(expected_result, actual_result)

    def test_get_possible_moves1(self):
        expected_result = ['a2', 'a3']
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        connect4b.insert('X', 'c2')

        actual_result = connect4b.get_possible_moves()
        self.assertListEqual(sorted(expected_result), sorted(actual_result))

    def test_get_possible_moves2(self):
        expected_result = ['a2', 'a3', 'c2']
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        actual_result = connect4b.get_possible_moves()
        self.assertListEqual(sorted(expected_result), sorted(actual_result))

    def test_is_valid_move1(self):
        expected_result = True
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        actual_result = connect4b.is_valid_move('a2')
        self.assertEqual(expected_result, actual_result)

    def test_is_valid_move2(self):
        expected_result = False
        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'c1')

        connect4b.insert('X', 'b1')
        connect4b.insert('O', 'b3')

        actual_result = connect4b.is_valid_move('c1')
        self.assertEqual(expected_result, actual_result)

    def test_get_next_board_states1(self):
        expected_result = dict()

        for move in ['a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3']:
            connect4b = Connect4Board()
            connect4b.insert('X', 'b2')
            connect4b.insert('O', move)
            expected_result[move] = connect4b

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')

        actual_result = connect4b.get_next_board_states('O')

        for move, board in expected_result.items():
            self.assertIn(move, actual_result.keys())
            self.assertEqual(board, actual_result[move])

    def test_get_next_board_states2(self):
        expected_result = dict()

        for move in ['a1', 'b1', 'c1', 'a2', 'c2', 'b3', 'c3']:
            connect4b = Connect4Board()
            connect4b.insert('X', 'b2')
            connect4b.insert('O', 'a3')
            connect4b.insert('X', move)
            expected_result[move] = connect4b

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a3')

        actual_result = connect4b.get_next_board_states('X')

        for move, board in expected_result.items():
            self.assertIn(move, actual_result.keys())
            self.assertEqual(board, actual_result[move])

    def test_deep_copy1(self):

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a3')

        tttb_copy = connect4b.deep_copy()

        self.assertEqual(connect4b, tttb_copy)

    def test_get_binary_board1(self):

        expected_bb = [[[0, 0], [0, 0], [0, 0]],
                       [[0, 0], [1, 0], [0, 0]],
                       [[0, 0], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')

        actual_bb = connect4b.get_binary_board('X')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_binary_board2(self):

        expected_bb = [[[0, 0], [0, 0], [0, 0]],
                       [[0, 0], [0, 1], [0, 0]],
                       [[1, 0], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        actual_bb = connect4b.get_binary_board('O')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_binary_board3(self):

        expected_bb = [[[0, 0], [0, 0], [1, 0]],
                       [[0, 0], [1, 0], [0, 0]],
                       [[0, 1], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')
        connect4b.insert('X', 'c3')

        actual_bb = connect4b.get_binary_board('X')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_binary_board4(self):

        expected_bb = [[[1, 0], [0, 0], [0, 1]],
                       [[0, 0], [0, 1], [0, 0]],
                       [[1, 0], [0, 0], [0, 0]]]
        expected_bb = np.array(expected_bb)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')
        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'a3')

        actual_bb = connect4b.get_binary_board('O')

        np.testing.assert_array_equal(expected_bb, actual_bb)

    def test_get_pretty_board1(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        expected_pb = pretty_board.format(*pieces)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')

        actual_pb = connect4b.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)

    def test_get_pretty_board2(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = ['O', ' ', ' ', ' ', 'X', ' ', ' ',' ',' ']
        expected_pb = pretty_board.format(*pieces)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')

        actual_pb = connect4b.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)

    def test_get_pretty_board3(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = ['O', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        expected_pb = pretty_board.format(*pieces)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')
        connect4b.insert('X', 'c3')

        actual_pb = connect4b.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)

    def test_get_pretty_board4(self):

        pretty_board = "---------------------\n3 |  {6}  |  {7}  |  {8}  |\n--|-----|-----|-----|\n2 |  {3}  |  {4}  |  {5}  |\n--|-----|-----|-----|\n1 |  {0}  |  {1}  |  {2}  |\n--|-----|-----|-----|\n  |  a  |  b  |  c  |"
        pieces = ['O', ' ', ' ', ' ', 'X', ' ', 'O', ' ', 'X']
        expected_pb = pretty_board.format(*pieces)

        connect4b = Connect4Board()
        connect4b.insert('X', 'b2')
        connect4b.insert('O', 'a1')
        connect4b.insert('X', 'c3')
        connect4b.insert('O', 'a3')

        actual_pb = connect4b.get_pretty_board()

        self.assertEqual(expected_pb, actual_pb)


if __name__ == '__main__':
    unittest.main()
