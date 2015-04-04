from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.ships import AircraftCarrier, Battleship, Cruiser, Destroyer, Submarine


class ShipTestCase(TestCase):
    def assertShipPosition(self, ship, row, column):
        self.assertEqual(row, ship.row)
        self.assertEqual(column, ship.column)

    def assertShipPositionInvalid(self, sheet, shipClass, location, orientation):
        with self.assertRaises(IndexError):
            shipClass(sheet, location, orientation)


class AircraftCarrierTest(ShipTestCase):

    def setUp(self):
        self.sheet = GameSheet()

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(AircraftCarrier(self.sheet, 'A4', Horizontal), 'A', 4)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(AircraftCarrier(self.sheet, 'D1', Vertical), 'D', 1)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(self.sheet, AircraftCarrier, 'A5', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(self.sheet, AircraftCarrier, 'E1', Vertical)


class BattleshipTest(ShipTestCase):

    def setUp(self):
        self.sheet = GameSheet()

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(Battleship(self.sheet, 'A5', Horizontal), 'A', 5)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Battleship(self.sheet, 'E1', Vertical), 'E', 1)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(self.sheet, Battleship, 'A6', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(self.sheet, Battleship, 'F1', Vertical)


class CruiserTest(ShipTestCase):

    def setUp(self):
        self.sheet = GameSheet()

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(Cruiser(self.sheet, 'A6', Horizontal), 'A', 6)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Cruiser(self.sheet, 'F1', Vertical), 'F', 1)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(self.sheet, Cruiser, 'A7', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(self.sheet, Cruiser, 'G1', Vertical)


class DestroyerTest(ShipTestCase):

    def setUp(self):
        self.sheet = GameSheet()

    def test_should_parse_location_string_for_horizontal_location_for_horizontal_location(self):
        self.assertShipPosition(Destroyer(self.sheet, 'B7', Horizontal), 'B', 7)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Destroyer(self.sheet, 'G2', Vertical), 'G', 2)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(self.sheet, Destroyer, 'D8', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(self.sheet, Destroyer, 'H8', Vertical)


class SubmarineTest(ShipTestCase):

    def setUp(self):
        self.sheet = GameSheet()

    def test_should_parse_location_string_for_horizontal_location(self):
        self.assertShipPosition(Submarine(self.sheet, 'B8', Horizontal), 'B', 8)

    def test_should_parse_location_string_for_vertical_location(self):
        self.assertShipPosition(Submarine(self.sheet, 'G8', Vertical), 'G', 8)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(self.sheet, Submarine, 'D9', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(self.sheet, Submarine, 'I8', Vertical)

