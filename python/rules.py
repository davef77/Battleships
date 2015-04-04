from python.gameSheet import ROW_NAMES


class Rules:
    def __init__(self):
        self.ships = {}
        self.occupied_cells = set()

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

    def on_cell_occupied(self, row, column, value):
        self.occupied_cells.add("%s%s" % (row, column))

    def _assert_fits_on_sheet(self, sheet, ship):
        max_column = sheet.width - ship.orientation.width(ship.waterline_length, ship.beam) + 1
        max_row = sheet.height - ship.orientation.height(ship.waterline_length, ship.beam) + 1

        if not ROW_NAMES.__contains__(ship.row) or ROW_NAMES.index(ship.row) >= max_row or ship.column > max_column:
            raise Warning("Ship placed out of bounds")

    def _assert_is_placed_in_clear_space(self,ship):
        occupied_cells = self.occupied_cells
        self.occupied_cells = set()
        ship.orientation.place_ship(self, ship)

        if occupied_cells & self.occupied_cells:
            raise Warning("Ship conflicts with a previously placed ship")


        self.occupied_cells = occupied_cells

    def _assert_within_allowed_number_for_type(self, ship):
        if self.ships.has_key(ship.id) and self.ships[ship.id] == ship.max_of_type:
            raise Warning("Can't add more than %s %ss" % (ship.max_of_type, ship.__class__))

    def _mark_occupied_cells(self, ship):
        ship.orientation.place_ship(self, ship)
