from src.clocks.time_per_move_clock import TimePerMoveClock


class ClockFactory:
    __instance = None

    TIME_PER_MOVE_CLOCK = "_ClockFactory__time_per_move_clock"

    def __init__(self):
        if ClockFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__clocks = {}

    @staticmethod
    def get_instance():
        if ClockFactory.__instance is None:
            ClockFactory.__instance = ClockFactory()

        return ClockFactory.__instance

    def get_clock(self, *args, **kwargs):
        if 'clock_id' not in kwargs.keys():
            return self.__default(*args, **kwargs)

        clock_id = kwargs.pop('clock_id')
        clock = getattr(self, clock_id, self.__default)
        return clock(*args, **kwargs)

    def __time_per_move_clock(self, *args, **kwargs):
        return TimePerMoveClock(*args, **kwargs)

    def __default(self, *args, **kwargs):
        raise ValueError("No such clock exists.")
