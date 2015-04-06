from python.gameSheet import GameSheet
from python.rules import Rules


class BattleShips(object):

    def __init__(self, game_sheet_factory):
        self.game_sheet_factory = game_sheet_factory
        self.player1 = None
        self.player2 = None

    def new_game(self):
        self.player1 = self.game_sheet_factory.create_game_sheet()
        self.player2 = self.game_sheet_factory.create_game_sheet()


if __name__ == "__main__":
    battleships = BattleShips()

    print battleships.new_game()




