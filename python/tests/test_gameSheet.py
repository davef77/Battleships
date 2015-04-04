from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine

ROW_A_END = 9

ROW_D_START = 30
ROW_D_END = 39

ROW_E_START = 40
ROW_E_END = 49

EMPTY_GAME_SHEET = "A........\nB........\nC........\nD........\nE........\nF........\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_AIRCRAFTCARRIER = "A........\nB..A.....\nC..A.....\nD..A.....\nE..A.....\nF..A.....\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_BATTLESHIP = "A........\nB........\nC....B...\nD....B...\nE....B...\nF....B...\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_CRUISER = "A........\nB........\nC....C...\nD....C...\nE....C...\nF........\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_DESTROYER = "A........\nB........\nC....D...\nD....D...\nE........\nF........\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_SUBMARINE = "A........\nB........\nC....S...\nD........\nE........\nF........\nG........\nH........\n.12345678"


class GameSheetTest(TestCase):
    def setUp(self):
        self.game = GameSheet()

    def test_should_render_as_cartesian_plane(self):
        self.assertEqual(EMPTY_GAME_SHEET, str(self.game))

    def test_should_place_an_aircraft_carrier_horizontally(self):
        self.game.add_ship(AircraftCarrier(self.game, 'A1', Horizontal))

        self.assertEquals("AAAAAA...", str(self.game)[:ROW_A_END])

    def test_should_place_an_aircraft_carrier_vertically(self):
        self.game.add_ship(AircraftCarrier(self.game, 'B3', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_AIRCRAFTCARRIER, str(self.game))

    def test_should_reject_placement_of_second_aircraft_carrier(self):
        self.game.add_ship(AircraftCarrier(self.game, 'A1', Horizontal))
        with self.assertRaises(Warning):
            self.game.add_ship(AircraftCarrier(self.game, 'B2', Horizontal))

    def test_should_place_a_battleship_horizontally(self):
        self.game.add_ship(Battleship(self.game, 'D2', Horizontal))

        self.assertEquals("D.BBBB...", str(self.game)[ROW_D_START:ROW_D_END])

    def test_should_place_a_battleship_vertically(self):
        self.game.add_ship(Battleship(self.game, 'C5', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_BATTLESHIP, str(self.game))

    def test_should_reject_placement_of_second_battleship(self):
        self.game.add_ship(Battleship(self.game, 'A1', Horizontal))
        with self.assertRaises(Warning):
            self.game.add_ship(Battleship(self.game, 'B2', Horizontal))

    def test_should_place_a_cruiser_horizontally(self):
        self.game.add_ship(Cruiser(self.game, 'E3', Horizontal))

        self.assertEquals("E..CCC...", str(self.game)[ROW_E_START:ROW_E_END])

    def test_should_place_a_cruiser_vertically(self):
        self.game.add_ship(Cruiser(self.game, 'C5', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_CRUISER, str(self.game))

    def test_should_reject_cruiser_of_second_battleship(self):
        self.game.add_ship(Cruiser(self.game, 'A1', Horizontal))
        with self.assertRaises(Warning):
            self.game.add_ship(Cruiser(self.game, 'B2', Horizontal))

    def test_should_place_a_destroyer_horizontally(self):
        self.game.add_ship(Destroyer(self.game, 'E3', Horizontal))

        self.assertEquals("E..DD....", str(self.game)[ROW_E_START:ROW_E_END])

    def test_should_place_a_destroyer_vertically(self):
        self.game.add_ship(Destroyer(self.game, 'C5', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_DESTROYER, str(self.game))

    def test_should_reject_cruiser_of_third_destroyer(self):
        self.game.add_ship(Destroyer(self.game, 'A1', Horizontal))
        self.game.add_ship(Destroyer(self.game, 'B2', Vertical))
        with self.assertRaises(Warning):
            self.game.add_ship(Destroyer(self.game, 'B4', Horizontal))

    def test_should_place_a_submarine_horizontally(self):
        self.game.add_ship(Submarine(self.game, 'E3', Horizontal))

        self.assertEquals("E..S.....", str(self.game)[ROW_E_START:ROW_E_END])

    def test_should_place_a_submarine_vertically(self):
        self.game.add_ship(Submarine(self.game, 'C5', Vertical))

        self.assertEquals(GAME_SHEET_WITH_VERT_SUBMARINE, str(self.game))

    def test_should_reject_submarine_of_third_destroyer(self):
        self.game.add_ship(Submarine(self.game, 'A1', Horizontal))
        self.game.add_ship(Submarine(self.game, 'B2', Vertical))
        with self.assertRaises(Warning):
            self.game.add_ship(Submarine(self.game, 'B4', Horizontal))

