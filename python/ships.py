from python.gameSheet import ROW_NAMES


class Ship():
    def __init__(self, sheet, location, orientation):
        self.row, self.column = _parse_location(location)
        self.orientation = orientation
        self._assert_fits_on_sheet(sheet)

    def _assert_fits_on_sheet(self, sheet):
        max_column = sheet.width - self.orientation.width(self.waterline_length, self.beam) + 1
        max_row = sheet.height - self.orientation.height(self.waterline_length, self.beam) + 1

        if not ROW_NAMES.__contains__(self.row) or ROW_NAMES.index(self.row) >= max_row or self.column > max_column:
            raise IndexError("Ship placed out of bounds")


class AircraftCarrier(Ship):
    def __init__(self, sheet, location, orientation):
        self.id = 'A'
        self.waterline_length = 5
        self.beam = 1
        self.max_of_type = 1
        Ship.__init__(self, sheet, location, orientation)


class Battleship(Ship):
    def __init__(self, sheet, location, orientation):
        self.id = 'B'
        self.waterline_length = 4
        self.beam = 1
        self.max_of_type = 1
        Ship.__init__(self, sheet, location, orientation)


class Cruiser(Ship):
    def __init__(self, sheet, location, orientation):
        self.id = 'C'
        self.waterline_length = 3
        self.beam = 1
        self.max_of_type = 1
        Ship.__init__(self, sheet, location, orientation)


class Destroyer(Ship):
    def __init__(self, sheet, location, orientation):
        self.id = 'D'
        self.waterline_length = 2
        self.beam = 1
        self.max_of_type = 2
        Ship.__init__(self, sheet, location, orientation)


class Submarine(Ship):
    def __init__(self, sheet, location, orientation):
        self.id = 'S'
        self.waterline_length = 1
        self.beam = 1
        self.max_of_type = 2
        Ship.__init__(self, sheet, location, orientation)


def _parse_location(location):
    return location[:1], int(location[1:])




