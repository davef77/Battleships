from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.rules import Rules
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine


class ShipTestCase(TestCase):
    def setUp(self):
        self.sheet = GameSheet(Rules())

    def assertShipPosition(self, ship, row, column):
        self.assertEqual(row, ship.row)
        self.assertEqual(column, ship.column)


class AircraftCarrierTest(ShipTestCase):

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(AircraftCarrier('A4', Horizontal), 'A', 4)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(AircraftCarrier('D1', Vertical), 'D', 1)


class BattleshipTest(ShipTestCase):

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(Battleship('A5', Horizontal), 'A', 5)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Battleship('E1', Vertical), 'E', 1)


class CruiserTest(ShipTestCase):

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(Cruiser('A6', Horizontal), 'A', 6)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Cruiser('F1', Vertical), 'F', 1)


class DestroyerTest(ShipTestCase):

    def test_should_parse_location_string_for_horizontal_location_for_horizontal_location(self):
        self.assertShipPosition(Destroyer('B7', Horizontal), 'B', 7)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Destroyer('G2', Vertical), 'G', 2)


class SubmarineTest(ShipTestCase):

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(Submarine('B8', Horizontal), 'B', 8)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Submarine('G8', Vertical), 'G', 8)

