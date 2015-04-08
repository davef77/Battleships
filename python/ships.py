from python.game_utils import parse_location


class Result:
    def __eq__(self, other):
        return self.__class__ == other.__class__

class GameOver(Result): pass
class Hit(Result): pass
class Miss(Result): pass
class Sunk(Result): pass


class Ship():
    def __init__(self, location, orientation):
        self.row, self.column = parse_location(location)
        self.orientation = orientation
        self.hit_count = 0

    def hit(self):
        self.hit_count += 1

        if self.hit_count == self.waterline_length:
            return Sunk()
        else:
            return Hit()

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column and self.orientation == other.orientation


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







