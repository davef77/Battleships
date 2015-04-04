MAX_COLUMNS = 8
MAX_ROWS = 8

ROW_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class GameSheet:

    def __init__(self, rules):
        self.rules = rules
        self.sheet = {}
        self.width = MAX_COLUMNS
        self.height = MAX_ROWS

        self._init_sheet()

    def add_ship(self, ship):
        self.rules.assert_can_add_ship(self, ship)

        ship.orientation.place_ship(self, ship)

        self.rules.ship_added(ship)

    def set_cell_value(self, row, column, value):
        self.sheet[row][column] = value

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

    def _init_sheet(self):
        for row in ROW_NAMES:
            self.__init_row(row)



