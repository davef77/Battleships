from unittest import TestCase
from mock import MagicMock
from python.battleships import BattleShips
from python.game_sheet_factory import GameSheetFactory


class BattleShipsTest(TestCase):

    def setUp(self):
        self.factory = MagicMock(spec=GameSheetFactory)
        self.battleships = BattleShips(self.factory)

        self.battleships.new_game()

    def test_should_start_game_by_creating_player1_and_player2_game_sheets(self):

        self.factory.create_game_sheet.assert_called_once()

        self.assertEqual(2, self.factory.create_game_sheet.call_count)
