from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.rules import Rules
from python.ships import AircraftCarrier, Submarine, Hit, Miss

ROW_A_END = 9

ROW_E_START = 40
ROW_E_END = 49

EMPTY_GAME_SHEET = "A........\nB........\nC........\nD........\nE........\nF........\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_AIRCRAFTCARRIER = "A........\nB..A.....\nC..A.....\nD..A.....\nE..A.....\nF..A.....\nG........\nH........\n.12345678"
GAME_SHEET_WITH_VERT_SUBMARINE = "A........\nB........\nC....S...\nD........\nE........\nF........\nG........\nH........\n.12345678"
GAME_SHEET_WITH_HIT_AIRCRAFT_CARRIER = "AXAXAA...\nB.x.x....\nC........\nD........\nE........\nF........\nG........\nH........\n.12345678"


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

        self._assert_ships_placed(self.game, {'A': 5, 'B': 4, 'C': 3, 'D': 4, 'S': 2})

    def test_should_place_shot(self):
        self.game.fire("A1")

        self.assertEquals("Ax.......", str(self.game)[:ROW_A_END])

    def test_should_record_a_hit(self):
        self.game.add_ship(AircraftCarrier('A1', Horizontal))
        self.assertIsInstance(self.game.fire("A1"), Hit)

    def test_should_record_a_miss(self):
        self.game.add_ship(AircraftCarrier('A1', Horizontal))
        self.assertIsInstance(self.game.fire("B1"), Miss)

    def test_should_show_record_of_hits_and_misses(self):
        self.game.add_ship(AircraftCarrier('A1', Horizontal))
        self.game.fire("B2")
        self.game.fire("B4")
        self.game.fire("A1")
        self.game.fire("A3")

        self.assertEquals(GAME_SHEET_WITH_HIT_AIRCRAFT_CARRIER, str(self.game))


    def _assert_ships_placed(self, game, expected_ships):
        sheet = self._clean_sheet(game)

        count = self._init_count(expected_ships)

        self._count_ships(count, expected_ships, sheet)

        for key in count.iterkeys():
            self.assertEqual(count[key], expected_ships[key], "Count for '%s' doesn't match" % key)

    def _clean_sheet(self, game):
        sheet = list(str(game).replace("12345678", ""))
        for i in range(0, sheet.__len__(), 10):
            sheet[i] = '.'
        return sheet

    def _init_count(self, expected_ships):
        count = {}
        for ship in expected_ships.iterkeys():
            count[ship] = 0
        return count

    def _count_ships(self, count, expected_ships, sheet):
        for ship in sheet:
            if expected_ships.has_key(ship):
                count[ship] += 1

