from unittest import TestCase
from python.gameSheet import GameSheet
from python.orientation import Horizontal, Vertical
from python.ships import AircraftCarrier


class AircraftCarrierTest(TestCase):

    def setUp(self):
        self.sheet = GameSheet()

    def test_should_parse_location_string(self):
        self.assertShipPosition(AircraftCarrier(self.sheet, 'A1', Horizontal), 'A', 1)
        self.assertShipPosition(AircraftCarrier(self.sheet, 'B2', Horizontal), 'B', 2)
        self.assertShipPosition(AircraftCarrier(self.sheet, 'C3', Horizontal), 'C', 3)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(self.sheet, 'A4', Horizontal)
        self.assertShipPositionInvalid(self.sheet, 'C6', Horizontal)
        self.assertShipPositionInvalid(self.sheet, 'E8', Horizontal)

    def test_should_throw_exception_when_adding_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(self.sheet, 'D1', Vertical)
        self.assertShipPositionInvalid(self.sheet, 'F2', Vertical)
        self.assertShipPositionInvalid(self.sheet, 'G3', Vertical)

    def assertShipPositionInvalid(self, sheet, location, orientation):
        with self.assertRaises(IndexError):
            AircraftCarrier(sheet, location, orientation)

    def assertShipPosition(self, ship, row, column):
        self.assertEqual(row, ship.row)
        self.assertEqual(column, ship.column)

