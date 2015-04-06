class Ship():
    def __init__(self, location, orientation):
        self.row, self.column = _parse_location(location)
        self.orientation = orientation


class AircraftCarrier(Ship):
    def __init__(self, location, orientation):
        self.id = 'A'
        self.waterline_length = 5
        self.beam = 1
        self.max_of_type = 1
        Ship.__init__(self, location, orientation)


class Battleship(Ship):
    def __init__(self, location, orientation):
        self.id = 'B'
        self.waterline_length = 4
        self.beam = 1
        self.max_of_type = 1
        Ship.__init__(self, location, orientation)


class Cruiser(Ship):
    def __init__(self, location, orientation):
        self.id = 'C'
        self.waterline_length = 3
        self.beam = 1
        self.max_of_type = 1
        Ship.__init__(self, location, orientation)


class Destroyer(Ship):
    def __init__(self, location, orientation):
        self.id = 'D'
        self.waterline_length = 2
        self.beam = 1
        self.max_of_type = 2
        Ship.__init__(self, location, orientation)


class Submarine(Ship):
    def __init__(self, location, orientation):
        self.id = 'S'
        self.waterline_length = 1
        self.beam = 1
        self.max_of_type = 2
        Ship.__init__(self, location, orientation)


def _parse_location(location):
    return location[:1], int(location[1:])




