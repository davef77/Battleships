from unittest import TestCase
from python.battleships import BattleShips
from python.gameSheet import GameSheet


class BattleShipsTest(TestCase):

    def test_should_create_game(self):
        self.battleships = BattleShips()

        game = self.battleships.new_game()

        self.assertIsInstance(game, GameSheet)