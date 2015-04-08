from python.game_utils import random_location
from python.orientation import Horizontal, Vertical
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine, GameOver
from python.game_stats_repository import GameStatsRepository


class BattleShips(object):

    def __init__(self, game_sheet_factory, game_stats_repo, player1, player2):
        self.game_sheet_factory = game_sheet_factory
        self.game_stats_repo = game_stats_repo
        self.players = {player1: None, player2: None}
        self.scores = {}
        self.computer_player = "Computer" in [player1, player2]
        self.scores[player1] = 0
        self.scores[player2] = 0

    def new_game(self):
        for player in self.players:
            self.players[player] = self.game_sheet_factory.create_game_sheet()

    def place_ship(self, player, ship_details):
        self.players[player].add_ship(self._create_ship(ship_details))

    def fire(self, player, location):
        fire_result = self._other_players_sheet(player).fire(location)

        if isinstance(fire_result, GameOver):
            self._end_game(player)

        self._computers_move(player)

        return fire_result

    def show_defense(self, player):
        return str(self.players[player])

    def show_offense(self, player):
        return str(self._other_players_sheet(player).hits_and_misses())

    def score(self, player):
        return self.scores[player]

    def _create_ship(self, ship_details):
        ship_class, location, orientation = parse_ship_details(ship_details)
        return ship_class(location, orientation)

    def _computers_move(self, player):
        if self.computer_player:
            self.players[player].fire(random_location())

    def _end_game(self, player):
        self.scores[player] += 1
        self.game_stats_repo.store_game_result(player, self._other_player(player))
        raise Warning("Game Over - %s Wins!" % player)

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
    battleships = BattleShips(GameStatsRepository())

    print battleships.new_game()




