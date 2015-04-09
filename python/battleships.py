from python.orientation import Horizontal, Vertical
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine


class BattleShips(object):

    def __init__(self, game_sheet_factory):
        self.game_sheet_factory = game_sheet_factory
        self.sheet = None

    def new_game(self):
        self.sheet = self.game_sheet_factory.create_game_sheet()

    def place_ship(self, ship_details):
        ship = self._create_ship(ship_details)
        self.sheet.add_ship(ship)

    def _create_ship(self, ship_details):
        ship_class, location, orientation = parse_ship_details(ship_details)
        return ship_class(location, orientation)


def parse_ship_details(ship_details):
    return _ship_type(ship_details[0:1]), ship_details[1:3], _orientation(ship_details[-1:])


def _ship_type(type):
    if type is 'A':
        return AircraftCarrier
    elif type is 'B':
        return Battleship
    elif type is 'C':
        return Cruiser
    elif type is 'D':
        return Destroyer
    elif type is 'S':
        return Submarine


def _orientation(orientation):
    if orientation is 'H':
        return Horizontal
    else:
        return Vertical
