from abc import abstractmethod


class Player:

    def __init__(self, name: str = "Player"):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def move(self, game):
        pass

    def __eq__(self, other):
        return hasattr(other, 'name') and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
