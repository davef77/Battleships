from random import randint, choice
from python.game_utils import parse_location
from python.orientation import ORIENTATIONS

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

    def fire(self, location):
        row, column = parse_location(location)
        self._set_cell_value(row, column, 'x')

    def position_ships(self):
        for ship_type in self.rules.list_ship_types():
            self._place_ship_at_random_position(ship_type)

    def on_cell_occupied(self, row, column, value):
        self._set_cell_value(row, column, value)

    def _cell_value(self, row, column):
        return self.sheet[row][column]

    def _set_cell_value(self, row, column, value):
        self.sheet[row][column - 1] = value

    def __str__(self):
        sheet = ""

        for row in ROW_NAMES:
            sheet = self.__render_row(row, sheet)

        sheet += self.__footer()

        return sheet

    def __render_row(self, row, sheet):
        sheet += row

        for column in range(0, MAX_COLUMNS):
            sheet += self._cell_value(row, column)

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

    def _place_ship_at_random_position(self, ship_type):
        while True:
            try:
                self.add_ship(ship_type(self._random_location(), self._random_orientation()))
            except Warning:
                continue
            break

    def _random_location(self):
        return "%s%s" % (choice(ROW_NAMES), randint(1, 8))

    def _random_orientation(self):
        return choice(ORIENTATIONS)



