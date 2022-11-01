class InvalidMoveException(Exception):

    def __init__(self, message, errors={}):
        super().__init__(message)
        self.errors = errors


class TimeoutException(Exception):

    def __init__(self, message, errors={}):
        super().__init__(message)
        self.errors = errors


class InvalidBoardException(Exception):
    def __init__(self, message, errors={}):
        super().__init__(message)
        self.errors = errors


class ClockNotTickingException(Exception):
    def __init__(self, message, errors={}):
        super().__init__(message)
        self.errors = errors


class UnSupportedException(Exception):
    def __init__(self, message, errors={}):
        super().__init__(message)
        self.errors = errors
