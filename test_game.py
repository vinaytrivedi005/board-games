from src.boards.board_factory import BoardFactory
from src.clocks.clock_factory import ClockFactory
from src.evaluators.evaluator_factory import EvaluatorFactory
from src.expanders.expander_factory import ExpanderFactory
from src.games.game_factory import GameFactory
from src.players.player_factory import PlayerFactory
from src.utilities import utility

utility.setup_logger()


def test(game_no):
    board = BoardFactory.get_instance().get_board(board_id=BoardFactory.TIC_TAC_TOE_BOARD)

    ev1 = EvaluatorFactory.get_instance().get_evaluator(evaluator_id=EvaluatorFactory.BOARD_STATE_EVALUATOR)
    ev2 = EvaluatorFactory.get_instance().get_evaluator(evaluator_id=EvaluatorFactory.RANDOM_SIMULATION_EVALUATOR)

    ex1 = ExpanderFactory.get_instance().get_expander(expander_id=ExpanderFactory.RANDOM_EXPANDER, evaluator=ev1)
    ex2 = ExpanderFactory.get_instance().get_expander(expander_id=ExpanderFactory.RANDOM_EXPANDER, evaluator=ev2)

    # tp1 = PlayerFactory.get_instance().get_player(ex1 if game_no % 2 == 0 else ex2,
    #                                               player_id=PlayerFactory.GENERAL_PLAYER, name="gp1")
    tp1 = PlayerFactory.get_instance().get_player(player_id=PlayerFactory.HUMAN_PLAYER, name="hp1")
    # tp2 = PlayerFactory.get_instance().get_player(ex1 if game_no % 2 == 1 else ex2,
    #                                               player_id=PlayerFactory.GENERAL_PLAYER, name="gp2")
    tp2 = PlayerFactory.get_instance().get_player(player_id=PlayerFactory.HUMAN_PLAYER, name="hp2")

    c1 = ClockFactory.get_instance().get_clock(clock_id=ClockFactory.TIME_PER_MOVE_CLOCK, time_per_move=60,
                                               stop_time_delta=1e-8)
    c2 = ClockFactory.get_instance().get_clock(clock_id=ClockFactory.TIME_PER_MOVE_CLOCK, time_per_move=60,
                                               stop_time_delta=1e-8)

    tg = GameFactory.get_instance().get_game(board, [tp1, tp2], [tp1, tp2], {tp1: c1, tp2: c2},
                                             game_id=GameFactory.TIMED_GAME)
    result = tg.play(verbose=True)
    print(result)


if __name__ == '__main__':
    for i in range(1, 2):
        print('GAME:', i)
        test(i)
