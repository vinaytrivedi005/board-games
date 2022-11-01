from abc import abstractmethod

from src.utilities.exceptions import UnSupportedException


class Clock:

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def time_for_move(self):
        pass

    @abstractmethod
    def is_stop_time(self):
        pass

    def convert(self, t, source_unit, target_unit):
        if source_unit == 'ns' and target_unit == 's':
            return self.__convert_ns_to_s(t)

        raise UnSupportedException(f"time conversion from {source_unit} to {target_unit} is not supported.")

    def __convert_ns_to_s(self, t):
        factor = 1e9

        return int(t/factor)
