from src.boards.tic_tac_toe_board import TicTacToeBoard


class BoardFactory:
    __instance = None

    TIC_TAC_TOE_BOARD = "_BoardFactory__tic_tac_toe_board"

    def __init__(self):
        if BoardFactory.__instance is not None:
            raise NotImplementedError("singleton class cannot be instantiated")
        self.__boards = {}

    @staticmethod
    def get_instance():
        if BoardFactory.__instance is None:
            BoardFactory.__instance = BoardFactory()

        return BoardFactory.__instance

    def get_board(self, *args, **kwargs):
        if 'board_id' not in kwargs.keys():
            return self.__default(*args, **kwargs)

        board_id = kwargs.pop('board_id')
        board = getattr(self, board_id, self.__default)
        return board(*args, **kwargs)

    def __tic_tac_toe_board(self, *args, **kwargs):
        return TicTacToeBoard(*args, **kwargs)

    def __default(self, *args, **kwargs):
        raise ValueError("No such board exists.")
