import time

from src.clocks.clock import Clock
from src.utilities.exceptions import ClockNotTickingException


class TimePerMoveClock(Clock):

    def __init__(self, time_per_move=60, stop_time_delta=1):
        super().__init__()
        self.__start_time = None
        self.__time_per_move = time_per_move * (10**9)
        self.__stop_time_delta = stop_time_delta * (10**9)

    def start(self):
        start_time = time.time_ns()
        self.__start_time = start_time

    def stop(self):
        self.__start_time = None

    def time_for_move(self):
        if self.__start_time is None:
            raise ClockNotTickingException("clock must be ticking to know time for move")

        current_time = time.time_ns()
        elapsed_time = current_time - self.__start_time
        return self.__time_per_move - elapsed_time

    def is_stop_time(self):
        time_for_move = self.time_for_move()

        if time_for_move <= self.__stop_time_delta:
            return True

        return False
