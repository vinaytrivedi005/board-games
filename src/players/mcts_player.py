import logging
import math
import random
from queue import Queue

from src.games.game import Game
from src.players.player import Player
from src.players.random_player import RandomPlayer

logger = logging.getLogger(__name__)
log = logger.log

"""
out of 150 game simulation with max visit count as 1000, 10000, 10000, mcts scores 128-16-6 against random player.

lost games:

lost as X game moves:
lost as O game moves:
moves: ['a2', 'c3', 'b3', 'b2', 'a1', 'c1', 'a3'], visit count: 1000
moves: ['b1', 'b2', 'c3', 'c1', 'a3', 'a2', 'b3'], visit count: 10000
moves: ['b2', 'a1', 'c2', 'c1', 'b1', 'a2', 'b3'], visit count: 10000
moves: ['b1', 'b2', 'a3', 'c3', 'a1', 'c2', 'a2'], visit count: 10000
moves: ['b3', 'b2', 'a2', 'c3', 'a1', 'c1', 'a3'], visit count: 100000
moves: ['c1', 'b2', 'a2', 'c3', 'a1', 'b3', 'b1'], visit count: 100000

"""


class MCTSPlayer(Player):

    def __init__(self, name: str = "MCTSPlayer"):
        super().__init__(name=name)
        self.__root = None
        self.__max_visit_count = 1000

    def move(self, game):
        if self.__root is None or game.board != self.__root.board:
            self.__update_root(game.board)
            log(logging.INFO, f"updated root: {self.__root}")

        if self.__root.visit_count >= self.__max_visit_count:
            log(logging.INFO, f"reached max visit limit of {self.__max_visit_count} on node: {self.__root}")
            return self.__get_best_move()

        while self.__root.visit_count < self.__max_visit_count:
            log(logging.DEBUG, f"root: {self.__root}")
            node = self.__select(self.__root)
            log(logging.INFO, f"selected node: {node}")
            if node.board.is_terminal_state():
                result = node.board.evaluate()
            else:
                log(logging.DEBUG, f"expanding node: {node}")
                self.__expand(node)
                node = random.choice(node.children)
                log(logging.DEBUG, f"random play node: {node}")
                result = self.__random_play(node)
            log(logging.INFO, f"back propagating result: {result} from node: {node}")
            self.__back_propagate(node, result)

        return self.__get_best_move()

    def __evaluate(self, result, node):
        if result == 0:
            return 0
        elif result == 1:
            winning_piece = node.board.pieces[0]
        else:
            winning_piece = node.board.pieces[1]
        if node.maximizer_mark == winning_piece and node.is_maximizing:
            return 1
        if node.maximizer_mark == winning_piece and not node.is_maximizing:
            return -1
        if node.maximizer_mark != winning_piece and node.is_maximizing:
            return -1
        if node.maximizer_mark != winning_piece and not node.is_maximizing:
            return 1

    def __get_best_move(self):
        if self.__root is None or not self.__root.children:
            return None

        log(logging.INFO, f"(moves, scores, visits, wins): {[(c.move, c.score(), c.visit_count, c.win_count) for c in self.__root.children]}")

        node = min(self.__root.children, key=lambda child: child.score())
        log(logging.INFO, f"node: {node} - best move: {node.move}")
        return node.move

    def __update_root(self, board):
        if self.__root is None:
            self.__root = self.__create_node(board.deep_copy(), maximizer_mark=board.turn, is_maximizing=True)
        node = self.__find_node_from_board(board, self.__root)

        if node is None:
            node = self.__create_node(board.deep_copy(), maximizer_mark=self.__root.maximizer_mark,
                                      is_maximizing=board.turn == self.__root.maximizer_mark)
        else:
            node.parent = None
            node.move = None

        self.__root = node

    def __find_node_from_board(self, board, node):

        q = Queue()
        q.put(node)

        while not q.empty():
            node = q.get()
            if node.board == board:
                return node
            for child in node.children:
                q.put(child)

    def __select(self, node):
        while node.children:
            log(logging.DEBUG,
                f"node: {node}, "
                f"uct scores: {[self.__uct(c.win_count, c.visit_count, c.parent.visit_count) for c in node.children]}")
            node = max(node.children,
                       key=lambda child: self.__uct(child.win_count, child.visit_count, child.parent.visit_count))

        return node

    def __expand(self, node):
        board = node.board

        possible_moves = board.get_possible_moves()

        for move in possible_moves:
            b = board.deep_copy()
            b.insert(move)
            child = self.__create_node(b, maximizer_mark=self.__root.maximizer_mark, parent=node, move=move,
                                       is_maximizing=not node.is_maximizing)
            log(logging.DEBUG, f"new node: {child}")
            node.children.append(child)

    def __back_propagate(self, node, result):
        while node is not None:
            log(logging.DEBUG, f"back prop, updating node: {node} with result: {result}")
            node.visit_count += 1
            node_result = self.__evaluate(result, node)
            log(logging.DEBUG, f"back prop, node result: {node_result}")
            if node_result == 1:
                node.win_count += 1
            log(logging.DEBUG, f"back prop, updated node: {node}")
            node = node.parent

    def __random_play(self, node):
        board = node.board.deep_copy()
        log(logging.DEBUG, f"{board.get_pretty_board()}")

        if board.is_terminal_state():
            return board.evaluate()

        p1 = RandomPlayer()
        p2 = RandomPlayer()

        g = Game(board, [p1, p2], [p1, p2])

        result = g.play(verbose=False)
        return result

    def __uct(self, win_count, visit_count, parent_visit_count, c=1.41):
        """
        :param win_count: number of wins when the node was chosen
        :param visit_count: number of times the node was chosen
        :param parent_visit_count: number of times the parent of the node was chosen
        :param c: exploration constant, theoretically sqrt(2) is a good choice
        """
        if visit_count == 0:
            return math.inf

        exploitation_factor = win_count / visit_count
        exploration_factor = c * math.sqrt(math.log(parent_visit_count) / visit_count)
        return exploitation_factor + exploration_factor

    def __create_node(self, board, maximizer_mark, is_maximizing=False, parent=None, move=None, visit_count=0,
                      win_count=0):
        return MCTSPlayer.Node(board, maximizer_mark, is_maximizing=is_maximizing, parent=parent, move=move,
                               visit_count=visit_count, win_count=win_count)

    class Node:

        def __init__(self, board, maximizer_mark, is_maximizing=False, move=None, parent=None, visit_count=0,
                     win_count=0):
            self.board = board
            self.maximizer_mark = maximizer_mark
            self.is_maximizing = is_maximizing
            self.move = move
            self.visit_count = visit_count
            self.win_count = win_count
            self.parent = parent
            self.children = list()

        def score(self):
            if self.visit_count == 0:
                return 0

            return self.win_count / self.visit_count

        def __str__(self):
            return f"(board: {self.board}, maximizer_mark: {self.maximizer_mark}, maximizing: {self.is_maximizing}, " \
                   f"move: {self.move}, visit: {self.visit_count}, win: {self.win_count})"

        def __repr__(self):
            return f"(board: {self.board}, maximizer_mark: {self.maximizer_mark}, maximizing: {self.is_maximizing}, " \
                   f"move: {self.move}, visit: {self.visit_count}, win: {self.win_count})"
