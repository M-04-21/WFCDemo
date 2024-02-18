from . import Field
from . import Options
from .CollapseException import CollapseException

from random import choice
from sys import exit

class App:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.field = Field.field(rows, columns)

    def start(self):
        while True:
            try:
                for i in range(self.rows*self.columns):
                    self._collapse()
                self._printField()
                break
            except KeyboardInterrupt:
                print('[ Exited by user ]')
                exit(0)
            except CollapseException:
                print('[ Collapse Error ]')
                self.field = Field.field(self.rows, self.columns)
                

    def _collapse(self):
        ## TODO: Add multiprocesing
        # Get copy of Field
        field_copy = [ el for row in self.field for el in row ]
        # Sort and filter values
        field_copy.sort(key=lambda el: el.entropy)
        field_copy = list( filter(lambda el: el.entropy > 0, field_copy) )
        # Get least entropy Cell
        least_entropy_cell = field_copy[0]
        # Filter
        field_copy_least = list( filter(lambda el: el.entropy == least_entropy_cell.entropy,field_copy) )
        field_copy_least = list( filter(lambda el: not el.collapsed,field_copy_least) )
        # Pick random
        pick = choice(field_copy_least)
        pick.collapse()

        # Propogate changes
        if(pick.x > 0):
            self.field[pick.y][pick.x - 1].reduce( Options.rules[pick.value], Options.chances[pick.value] )
        if(pick.x < self.columns-1):
            self.field[pick.y][pick.x + 1].reduce( Options.rules[pick.value], Options.chances[pick.value]  )
        if(pick.y > 0):
            self.field[pick.y - 1][pick.x].reduce( Options.rules[pick.value], Options.chances[pick.value]  )
        if(pick.y < self.rows-1):
            self.field[pick.y + 1][pick.x].reduce( Options.rules[pick.value], Options.chances[pick.value]  )
        
        

    def _printField(self):
        COLOR_DICT = {
            'DeepWater': '\033[44m',
            'Water': '\033[46m',
            'Coast': '\033[43m',
            'Grass': '\033[42m',
            'Forest': '\033[47m',
            'clear': '\033[0m'
        }
        for row in range(self.rows):
            for column in range(self.columns):
                print(f'{COLOR_DICT[self.field[row][column].value]} {COLOR_DICT["clear"]}', end='')
            print()
