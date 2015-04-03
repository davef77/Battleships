from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal
from python.ships import AircraftCarrier

EMPTY_GAME_SHEET = "A........\nB........\nC........\nD........\nE........\nF........\nG........\nH........\n.12345678"""


class GameSheetTest(TestCase):

    def setUp(self):
        self.game = GameSheet()

    def test_should_render_as_cartesian_plane(self):
        self.assertEqual(EMPTY_GAME_SHEET, str(self.game))

    def test_should_place_an_aircraft_carrier_horizontally(self):
        self.game.place_ship(AircraftCarrier(self.game, 'A1', Horizontal))

        self.assertEquals("AAAAAA...", str(self.game)[:9])