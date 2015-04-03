from unittest import TestCase
from python.gameSheet import GameSheet

EMPTY_GAME_SHEET = "A........\nB........\nC........\nD........\nE........\nF........\nG........\nH........\n.12345678"""


class GameSheetTest(TestCase):

    def setUp(self):
        self.game = GameSheet()

    def test_should_render_as_cartesian_plane(self):
        self.assertEqual(EMPTY_GAME_SHEET, str(self.game))
