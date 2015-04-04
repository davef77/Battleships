from python.gameSheet import GameSheet
from python.rules import Rules


class BattleShips(object):

    def new_game(self):
        return GameSheet(Rules())


if __name__ == "__main__":
    battleships = BattleShips()

    print battleships.new_game()




