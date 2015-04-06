from python.gameSheet import ROW_NAMES
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine, Miss, Sunk


class Rules:
    def __init__(self):
        self.ships = {}
        self.occupied_cells = {}
        self.ship_being_placed = None

    def assert_can_add_ship(self, sheet, ship):
        self._assert_fits_on_sheet(sheet, ship)
        self._assert_is_placed_in_clear_space(ship)
        self._assert_within_allowed_number_for_type(ship)

    def ship_added(self, ship):
        if self.ships.has_key(ship.id):
            self.ships[ship.id] += 1
        else:
            self.ships[ship.id] = 1

        self._mark_occupied_cells(ship)

    def fire(self, location):
        if self.occupied_cells.has_key(location):
            return self._process_hit(location)
        else:
            return Miss()

    def list_ship_types(self):
        return [AircraftCarrier, Battleship, Cruiser, Destroyer, Destroyer, Submarine, Submarine]

    def on_cell_occupied(self, row, column, value):
        self.occupied_cells["%s%s" % (row, column)] = self.ship_being_placed

    def _mark_occupied_cells(self, ship):
        self.ship_being_placed = ship
        ship.orientation.place_ship(self, ship)

    def _process_hit(self, location):
        hit_ship = self.occupied_cells[location]
        hit_result = hit_ship.hit()
        if isinstance(hit_result, Sunk):
            self._remove_ship(hit_ship)
        return hit_result

    def _assert_fits_on_sheet(self, sheet, ship):
        max_column = sheet.width - ship.orientation.width(ship.waterline_length, ship.beam) + 1
        max_row = sheet.height - ship.orientation.height(ship.waterline_length, ship.beam) + 1

        if not ROW_NAMES.__contains__(ship.row) or ROW_NAMES.index(ship.row) >= max_row or ship.column > max_column:
            raise Warning("Ship placed out of bounds")

    def _assert_is_placed_in_clear_space(self, ship):
        occupied_cells = self.occupied_cells
        try:
            self.occupied_cells = {}
            ship.orientation.place_ship(self, ship)

            if set(occupied_cells.keys()) & set(self.occupied_cells.keys()):
                raise Warning("Ship conflicts with a previously placed ship")
        finally:
            self.occupied_cells = occupied_cells

    def _assert_within_allowed_number_for_type(self, ship):
        if self.ships.has_key(ship.id) and self.ships[ship.id] == ship.max_of_type:
            raise Warning("Can't add more than %s %ss" % (ship.max_of_type, ship.__class__))

    def _remove_ship(self, hit_ship):
        for cell in self.occupied_cells.items():
            if cell[1] == hit_ship:
                del self.occupied_cells[cell[0]]
