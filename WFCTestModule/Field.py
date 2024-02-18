from . import Cell

def field(rows, columns):
    f = [ [Cell.Cell(column, row) for column in range(columns)] for row in range(rows) ]
    return f
