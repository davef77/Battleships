from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.rules import Rules
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine


class BattleShips(object):

    def __init__(self, game_sheet_factory):
        self.game_sheet_factory = game_sheet_factory
        self.players = {}

    def new_game(self, player1, player2):
        self.players[player1] = self.game_sheet_factory.create_game_sheet()
        self.players[player2] = self.game_sheet_factory.create_game_sheet()

    def place_ship(self, player, ship_details):
        self.players[player].add_ship(self._create_ship(ship_details))

    def fire(self, player, location):
        return self._other_players_sheet(player).fire(location)

    def show_defense(self, player):
        return str(self.players[player])

    def show_offense(self, player):
        return str(self._other_players_sheet(player).hits_and_misses())

    def _create_ship(self, ship_details):
        ship_class, location, orientation = parse_ship_details(ship_details)
        return ship_class(location, orientation)

    def _other_players_sheet(self, player):
        return self.players[self._other_player(player)]

    def _other_player(self, player):
        for key in self.players.keys():
            if key is not player:
                return key

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



if __name__ == "__main__":
    battleships = BattleShips()

    print battleships.new_game()




