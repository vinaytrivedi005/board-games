from src.evaluators.board_state_evaluator import BoardStateEvaluator
from src.evaluators.random_evaluator import RandomEvaluator
from src.evaluators.random_simulation_evaluator import RandomSimulationEvaluator


class EvaluatorFactory:
    __instance = None

    RANDOM_EVALUATOR = "_EvaluatorFactory__random_evaluator"
    RANDOM_SIMULATION_EVALUATOR = "_EvaluatorFactory__random_simulation_evaluator"
    BOARD_STATE_EVALUATOR = "_EvaluatorFactory__board_state_evaluator"

    def __init__(self):
        if EvaluatorFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__evaluators = {EvaluatorFactory.RANDOM_EVALUATOR: RandomEvaluator(),
                             EvaluatorFactory.RANDOM_SIMULATION_EVALUATOR: RandomSimulationEvaluator(),
                             EvaluatorFactory.BOARD_STATE_EVALUATOR: BoardStateEvaluator()}

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
        return self.__evaluators.get(EvaluatorFactory.RANDOM_EVALUATOR, self.__default)

    def __random_simulation_evaluator(self, *args, **kwargs):
        return self.__evaluators.get(EvaluatorFactory.RANDOM_SIMULATION_EVALUATOR, self.__default)

    def __board_state_evaluator(self, *args, **kwargs):
        return self.__evaluators.get(EvaluatorFactory.BOARD_STATE_EVALUATOR, self.__default)

    def __default(self, *args, **kwargs):
        raise ValueError("No such evaluator exists.")
