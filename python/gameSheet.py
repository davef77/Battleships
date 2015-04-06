from python.gameSheet_renderer import DefenseSheetRenderer, HitAndMissesSheetRenderer, MAX_COLUMNS, MAX_ROWS, ROW_NAMES
from python.game_utils import parse_location, random_location, random_orientation
from python.ships import Miss


class GameSheet:

    def __init__(self, rules):
        self.rules = rules
        self.offense_sheet_renderer = DefenseSheetRenderer()
        self.hits_and_misses_sheet_renderer = HitAndMissesSheetRenderer()
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
        fire_result = self.rules.fire(location)
        self._set_cell_value(row, column, self._format_fire_result(fire_result))

        return fire_result

    def position_ships(self):
        for ship_type in self.rules.list_ship_types():
            self._place_ship_at_random_position(ship_type)

    def hits_and_misses(self):
        return self.hits_and_misses_sheet_renderer.render_sheet(self.sheet)

    def on_cell_occupied(self, row, column, value):
        self._set_cell_value(row, column, value)

    def __str__(self):
        return self.offense_sheet_renderer.render_sheet(self.sheet)

    def _set_cell_value(self, row, column, value):
        self.sheet[row][column - 1] = value

    def _format_fire_result(self, result):
        if isinstance(result, Miss):
            return 'x'
        else:
            return 'X'

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
                self.add_ship(ship_type(random_location(), random_orientation()))
            except Warning:
                continue
            break



