from unittest import TestCase
from mock import MagicMock

from python.battleships import BattleShips
from python.game_sheet_factory import GameSheetFactory


class BattleShipsTest(TestCase):

    def test_should_create_new_game(self):
        mock_factory = MagicMock(GameSheetFactory)
        self.battleships = BattleShips(mock_factory)
        self.battleships.new_game()

        mock_factory.create_game_sheet.assert_called_with()
