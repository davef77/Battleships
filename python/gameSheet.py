from python.orientation import Horizontal

MAX_COLUMNS = 8
MAX_ROWS = 8

ROW_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class GameSheet:

    def __init__(self):
        self.sheet = {}
        self.width = MAX_COLUMNS
        self.height = MAX_ROWS

        for row in ROW_NAMES:
            self.__init_row(row)

    def place_ship(self, ship):
        if ship.orientation is Horizontal:
            for column in range(ship.column, ship.column + ship.waterline_length):
                self._set_cell_value(ship.row, column - 1, ship.id)

    def cell_value(self, row, column):
        return self.sheet[row][column]

    def __str__(self):
        sheet = ""

        for row in ROW_NAMES:
            sheet = self.__render_row(row, sheet)

        sheet += self.__footer()

        return sheet

    def __render_row(self, row, sheet):
        sheet += row

        for column in range(0, MAX_COLUMNS):
            sheet += self.cell_value(row, column)

        sheet += '\n'

        return sheet

    def __footer(self):
        footer = '.'

        for column in range(0, MAX_COLUMNS):
            footer += str(column + 1)

        return footer

    def __init_row(self, row):
        self.sheet[row] = []

        for column in range(0, MAX_COLUMNS):
            self.sheet[row].append('.')

    def _set_cell_value(self, row, column, value):
        self.sheet[row][column] = value
