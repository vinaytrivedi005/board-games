from src.evaluators.board_state_evaluator import BoardStateEvaluator
from src.evaluators.random_evaluator import RandomEvaluator
from src.evaluators.random_simulation_evaluator import RandomSimulationEvaluator
from src.evaluators.tic_tac_toe_nn_evaluator import TicTacToeNNEvaluator


class EvaluatorFactory:
    __instance = None

    RANDOM_EVALUATOR = "_EvaluatorFactory__random_evaluator"
    RANDOM_SIMULATION_EVALUATOR = "_EvaluatorFactory__random_simulation_evaluator"
    BOARD_STATE_EVALUATOR = "_EvaluatorFactory__board_state_evaluator"
    TIC_TAC_TOE_NN_EVALUATOR = "_EvaluatorFactory__tic_tac_toe_nn_evaluator"

    def __init__(self):
        if EvaluatorFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__evaluators = {}

    @staticmethod
    def get_instance():
        if EvaluatorFactory.__instance is None:
            EvaluatorFactory.__instance = EvaluatorFactory()

        return EvaluatorFactory.__instance

    def get_evaluator(self, *args, **kwargs):
        if 'evaluator_id' not in kwargs.keys():
            return self.__default(*args, **kwargs)

        evaluator_id = kwargs.pop('evaluator_id')
        evaluator = getattr(self, evaluator_id, self.__default)
        return evaluator(*args, **kwargs)

    def __random_evaluator(self, *args, **kwargs):
        return RandomEvaluator(*args, **kwargs)

    def __random_simulation_evaluator(self, *args, **kwargs):
        return RandomSimulationEvaluator(*args, **kwargs)

    def __board_state_evaluator(self, *args, **kwargs):
        return BoardStateEvaluator(*args, **kwargs)

    def __tic_tac_toe_nn_evaluator(self, *args, **kwargs):
        return TicTacToeNNEvaluator(*args, **kwargs)

    def __default(self, *args, **kwargs):
        raise ValueError("No such evaluator exists.")
