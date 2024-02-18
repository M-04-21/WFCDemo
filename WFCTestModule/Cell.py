from . import Options
from .CollapseException import CollapseException

from random import choices

class Cell:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._options = Options.options
        self._collapsed = False
        self._value = None
        self._chances = Options.defaultChances

    def reduce(self, rule, chances):
        self._chances = chances
        self._options = list( filter(lambda el: el in rule, self._options) )
        if(len(self._options) == 0):
            raise CollapseException()

    def collapse(self):
        if(not self._collapsed):
            self._collapsed = True
            weights = [self._chances[option] for option in self._options]
            self._value = choices(self._options, weights)[0]
        else:
            print(self)
            print('Cell already collapsed')

    @property
    def entropy(self):
        if(self._collapsed):
            return 0
        else:
            return len(self._options)
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    @property
    def collapsed(self):
        return self._collapsed
    @property
    def value(self):
        return self._value

    def __repr__(self):
        return str(self._value)
