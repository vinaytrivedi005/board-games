import random
import numpy as np

from src.boards.board_factory import BoardFactory
from src.clocks.clock_factory import ClockFactory
from src.evaluators.evaluator_factory import EvaluatorFactory
from src.expanders.expander_factory import ExpanderFactory
from src.games.game_factory import GameFactory
from src.players.player_factory import PlayerFactory
from src.utilities import utility

utility.setup_logger()


def train_model(num_games):
    ev_ids = [EvaluatorFactory.BOARD_STATE_EVALUATOR, EvaluatorFactory.RANDOM_SIMULATION_EVALUATOR,
              EvaluatorFactory.RANDOM_EVALUATOR, EvaluatorFactory.TIC_TAC_TOE_NN_EVALUATOR]
    ex_ids = [ExpanderFactory.RANDOM_EXPANDER, ExpanderFactory.EVALUATOR_BASED_EXPANDER]
    tp_ids = [PlayerFactory.GENERAL_PLAYER, PlayerFactory.TIMED_RANDOM_PLAYER]
    c_ids = [(ClockFactory.TIME_PER_MOVE_CLOCK, 60, 1e-8)]

    tic_tac_toe_nn_evaluator = EvaluatorFactory.get_instance().get_evaluator(
        evaluator_id=EvaluatorFactory.TIC_TAC_TOE_NN_EVALUATOR,
        model_path='D:/projects/board-games/resources/models/tic_tac_toe_nn_evaluator1.tf')
    X = list()
    y = list()
    for i in range(1, num_games + 1):
        print(f'GAME: {i}')

        board = BoardFactory.get_instance().get_board(board_id=BoardFactory.TIC_TAC_TOE_BOARD)

        ev_id1 = random.choice(ev_ids)
        ev_id2 = random.choice(ev_ids)

        ex_id1 = random.choice(ex_ids)
        ex_id2 = random.choice(ex_ids)

        tp_id1 = random.choice(tp_ids)
        tp_id2 = random.choice(tp_ids)

        c_id = random.choice(c_ids)

        ev1 = EvaluatorFactory.get_instance().get_evaluator(evaluator_id=ev_id1)
        ev2 = EvaluatorFactory.get_instance().get_evaluator(evaluator_id=ev_id2)

        ex1 = ExpanderFactory.get_instance().get_expander(expander_id=ex_id1, evaluator=ev1)
        ex2 = ExpanderFactory.get_instance().get_expander(expander_id=ex_id2, evaluator=ev2)

        tp1 = PlayerFactory.get_instance().get_player(expander=ex1, player_id=tp_id1, name="tp1")
        tp2 = PlayerFactory.get_instance().get_player(expander=ex2, player_id=tp_id2, name="tp2")

        c1 = ClockFactory.get_instance().get_clock(clock_id=c_id[0], time_per_move=c_id[1], stop_time_delta=c_id[2])
        c2 = ClockFactory.get_instance().get_clock(clock_id=c_id[0], time_per_move=c_id[1], stop_time_delta=c_id[2])

        tg = GameFactory.get_instance().get_game(board, [tp1, tp2], [tp1, tp2], {tp1: c1, tp2: c2},
                                                 game_id=GameFactory.TIMED_GAME)
        result = tg.play(verbose=True)
        print(result)
        nb = BoardFactory.get_instance().get_board(board_id=BoardFactory.TIC_TAC_TOE_BOARD)
        for move in tg.board.moves:
            nb.insert(move)
            X.append(nb.get_binary_board('X'))
            y.append(result)
        if i % 100 == 0:
            tic_tac_toe_nn_evaluator.train(np.array(X), np.array(y))
            X = list()
            y = list()


def test_model(num_games):
    ev_ids = [EvaluatorFactory.BOARD_STATE_EVALUATOR, EvaluatorFactory.RANDOM_SIMULATION_EVALUATOR,
              EvaluatorFactory.RANDOM_EVALUATOR, EvaluatorFactory.TIC_TAC_TOE_NN_EVALUATOR]
    ex_ids = [ExpanderFactory.RANDOM_EXPANDER, ExpanderFactory.EVALUATOR_BASED_EXPANDER]
    tp_ids = [PlayerFactory.GENERAL_PLAYER, PlayerFactory.TIMED_RANDOM_PLAYER]
    c_ids = [(ClockFactory.TIME_PER_MOVE_CLOCK, 60, 1e-8)]
    results = [0, 0, 0]
    for i in range(1, num_games + 1):
        # print(f'GAME: {i}')

        board = BoardFactory.get_instance().get_board(board_id=BoardFactory.TIC_TAC_TOE_BOARD)

        ev_id1 = random.choice(ev_ids)
        ev_id2 = EvaluatorFactory.TIC_TAC_TOE_NN_EVALUATOR

        ex_id1 = random.choice(ex_ids)
        ex_id2 = ExpanderFactory.EVALUATOR_BASED_EXPANDER

        tp_id1 = random.choice(tp_ids)
        tp_id2 = random.choice(tp_ids)

        c_id = random.choice(c_ids)

        ev1 = EvaluatorFactory.get_instance().get_evaluator(evaluator_id=ev_id1)
        ev2 = EvaluatorFactory.get_instance().get_evaluator(evaluator_id=ev_id2)

        ex1 = ExpanderFactory.get_instance().get_expander(expander_id=ex_id1, evaluator=ev1)
        ex2 = ExpanderFactory.get_instance().get_expander(expander_id=ex_id2, evaluator=ev2)

        tp1 = PlayerFactory.get_instance().get_player(expander=ex1 if i%2 == 1 else ex2, player_id=tp_id1, name="tp1")
        tp2 = PlayerFactory.get_instance().get_player(expander=ex2 if i%2 == 1 else ex1, player_id=tp_id2, name="tp2")

        c1 = ClockFactory.get_instance().get_clock(clock_id=c_id[0], time_per_move=c_id[1], stop_time_delta=c_id[2])
        c2 = ClockFactory.get_instance().get_clock(clock_id=c_id[0], time_per_move=c_id[1], stop_time_delta=c_id[2])

        tg = GameFactory.get_instance().get_game(board, [tp1, tp2], [tp1, tp2], {tp1: c1, tp2: c2},
                                                 game_id=GameFactory.TIMED_GAME)
        result = tg.play(verbose=False)
        # print(result)
        if result == 0:
            results[2] += 1
        elif result == 1:
            if i % 2 == 0:
                results[0] += 1
            else:
                results[1] += 1
        else:
            if i % 2 == 0:
                results[1] += 1
            else:
                results[0] += 1
    print(results)


if __name__ == '__main__':
    for j in range(10):
        # print('Training...')
        # train_model(1000)
        # print('#'*100)
        # print('Testing...')
        test_model(10)
