from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
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
        self.game = GameSheet()

    def test_should_render_as_cartesian_plane(self):
        self.assertEqual(EMPTY_GAME_SHEET, str(self.game))

    def test_should_place_an_aircraft_carrier_horizontally(self):
        self.game.add_ship(AircraftCarrier('A1', Horizontal))

        self.assertEquals("AAAAAA...", str(self.game)[:ROW_A_END])

    def test_should_place_an_aircraft_carrier_vertically(self):
        self.game.add_ship(AircraftCarrier('B3', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_AIRCRAFTCARRIER, str(self.game))

    def test_should_reject_placement_of_second_aircraft_carrier(self):
        self.game.add_ship(AircraftCarrier('A1', Horizontal))
        with self.assertRaises(Warning):
            self.game.add_ship(AircraftCarrier('B2', Horizontal))

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(AircraftCarrier, 'A5', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(AircraftCarrier, 'E1', Vertical)

    def test_should_place_a_submarine_horizontally(self):
        self.game.add_ship(Submarine('E3', Horizontal))

        self.assertEquals("E..S.....", str(self.game)[ROW_E_START:ROW_E_END])

    def test_should_place_a_submarine_vertically(self):
        self.game.add_ship(Submarine('C5', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_SUBMARINE, str(self.game))

    def test_should_reject_submarine_of_third_destroyer(self):
        self.game.add_ship(Submarine('A1', Horizontal))
        self.game.add_ship(Submarine('B2', Vertical))
        with self.assertRaises(Warning):
            self.game.add_ship(Submarine('B4', Horizontal))

    def test_should_throw_exception_when_adding_submarine_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(Submarine, 'D9', Horizontal)

    def test_should_throw_exception_when_adding_submarine_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(Submarine, 'I8', Vertical)

    def assertShipPositionInvalid(self, shipClass, location, orientation):
        with self.assertRaises(IndexError):
            self.game.add_ship(shipClass(location, orientation))

