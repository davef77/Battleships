from python.gameSheet import GameSheet


class BattleShips(object):

    def new_game(self):
        return GameSheet()


if __name__ == "__main__":
    battleships = BattleShips()

    print battleships.new_game()




