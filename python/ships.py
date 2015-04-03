from python.gameSheet import ROW_NAMES


class Ship():
    def __init__(self, sheet, location, orientation):
        self.row, self.column = _parse_location(location)
        self.orientation = orientation
        self._assert_fits_on_sheet(sheet)

    def _assert_fits_on_sheet(self, sheet):
        max_column = sheet.width - self.orientation.width(self.waterline_length, self.beam)
        if self.column > max_column:
            raise IndexError("Ship must be placed in a column less than %s" % max_column)

        max_row = sheet.height - self.orientation.height(self.waterline_length, self.beam)
        if ROW_NAMES.index(self.row) >= max_row:
            raise IndexError("Ship must be placed in a column less than %s" % max_column)


class AircraftCarrier(Ship):
    def __init__(self, sheet, location, orientation):
        self.id = 'A'
        self.waterline_length = 5
        self.beam = 1
        Ship.__init__(self, sheet, location, orientation)


def _parse_location(location):
    return location[:1], int(location[1:])




