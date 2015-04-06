from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.rules import Rules
from python.ships import AircraftCarrier, Submarine

ROW_A_END = 9

ROW_D_START = 30
ROW_D_END = 39

ROW_E_START = 40
ROW_E_END = 49

EMPTY_GAME_SHEET = "A........\nB........\nC........\nD........\nE........\nF........\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_AIRCRAFTCARRIER = "A........\nB..A.....\nC..A.....\nD..A.....\nE..A.....\nF..A.....\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_SUBMARINE = "A........\nB........\nC....S...\nD........\nE........\nF........\nG........\nH........\n.12345678"


class GameSheetTest(TestCase):
    def setUp(self):
        self.game = GameSheet(Rules())

    def test_should_render_as_cartesian_plane(self):
        self.assertEqual(EMPTY_GAME_SHEET, str(self.game))

    def test_should_place_an_aircraft_carrier_horizontally(self):
        self.game.add_ship(AircraftCarrier('A1', Horizontal))

        self.assertEquals("AAAAAA...", str(self.game)[:ROW_A_END])

    def test_should_place_an_aircraft_carrier_vertically(self):
        self.game.add_ship(AircraftCarrier('B3', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_AIRCRAFTCARRIER, str(self.game))

    def test_should_place_a_submarine_horizontally(self):
        self.game.add_ship(Submarine('E3', Horizontal))

        self.assertEquals("E..S.....", str(self.game)[ROW_E_START:ROW_E_END])

    def test_should_place_a_submarine_vertically(self):
        self.game.add_ship(Submarine('C5', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_SUBMARINE, str(self.game))

    def test_should_populate_with_ships(self):
        self.game.position_ships()

        sheet = list(str(self.game).replace("12345678", ""))

        for i in range(0, sheet.__len__(), 10):
            sheet[i] = '.'

        ships = {'A': 5, 'B': 4, 'C': 3, 'D': 4, 'S': 2}

        count = {}

        for ship in ships.iterkeys():
            count[ship] = 0

        for ship in sheet:
            if ships.has_key(ship):
                count[ship] += 1

        print self.game

        for key in count.iterkeys():
            self.assertEqual(count[key], ships[key], "Count for '%s' doesn't match" % key)