from python.gameSheet import ROW_NAMES


class Rules:
    def __init__(self):
        self.ships = {}

    def assert_can_add_ship(self, sheet, ship):
        self._assert_fits_on_sheet(sheet, ship)

        if self.ships.has_key(ship.id) and self.ships[ship.id] == ship.max_of_type:
            raise Warning("Can't add more than %s %ss" % (ship.max_of_type, ship.__class__))

    def ship_added(self, ship):
        if self.ships.has_key(ship.id):
            self.ships[ship.id] += 1
        else:
            self.ships[ship.id] = 1

    def _assert_fits_on_sheet(self, sheet, ship):
        max_column = sheet.width - ship.orientation.width(ship.waterline_length, ship.beam) + 1
        max_row = sheet.height - ship.orientation.height(ship.waterline_length, ship.beam) + 1

        if not ROW_NAMES.__contains__(ship.row) or ROW_NAMES.index(ship.row) >= max_row or ship.column > max_column:
            raise IndexError("Ship placed out of bounds")

