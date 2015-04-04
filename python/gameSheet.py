MAX_COLUMNS = 8
MAX_ROWS = 8

ROW_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class GameSheet:

    def __init__(self):
        self.sheet = {}
        self.width = MAX_COLUMNS
        self.height = MAX_ROWS
        self.ships = {}

        for row in ROW_NAMES:
            self.__init_row(row)

    def add_ship(self, ship):
        self._assert_can_add_ship(ship)

        ship.orientation.place_ship(self, ship)

        self._ship_added(ship)

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

    def _assert_can_add_ship(self, ship):
        self._assert_fits_on_sheet(ship)

        if self.ships.has_key(ship.id) and self.ships[ship.id] == ship.max_of_type:
            raise Warning("Can't add more than %s %ss" % (ship.max_of_type, ship.__class__))

    def _assert_fits_on_sheet(self, ship):
        max_column = self.width - ship.orientation.width(ship.waterline_length, ship.beam) + 1
        max_row = self.height - ship.orientation.height(ship.waterline_length, ship.beam) + 1

        if not ROW_NAMES.__contains__(ship.row) or ROW_NAMES.index(ship.row) >= max_row or ship.column > max_column:
            raise IndexError("Ship placed out of bounds")

    def _ship_added(self, ship):
        if self.ships.has_key(ship.id):
            self.ships[ship.id] += 1
        else:
            self.ships[ship.id] = 1

