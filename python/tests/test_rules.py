from unittest import TestCase
from mock import MagicMock
from python.orientation import Horizontal, Vertical
from python.rules import Rules
from python.ships import AircraftCarrier, Submarine, Cruiser


class RulesTest(TestCase):
    def setUp(self):
        self.rules = Rules()
        self.sheet = MagicMock()

        self.sheet.width = 8
        self.sheet.height = 8

    def test_should_reject_placement_of_second_aircraft_carrier(self):
        self.rules.ship_added(AircraftCarrier('A1', Horizontal))
        with self.assertRaises(Warning):
            self.rules.assert_can_add_ship(self.sheet, AircraftCarrier('B2', Horizontal))

    def test_should_reject_addition_of_ship_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(AircraftCarrier, 'A5', Horizontal)

    def test_should_reject_addition_of_ship_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(AircraftCarrier, 'E1', Vertical)

    def test_should_reject_placement_of_third_submarine(self):
        self.rules.ship_added(Submarine('A1', Horizontal))
        self.rules.ship_added(Submarine('B2', Vertical))
        with self.assertRaises(Warning):
            self.rules.assert_can_add_ship(self.sheet, Submarine('B4', Horizontal))

    def test_should_reject_addition_of_submarine_that_overflows_the_sheet_horizontally(self):
        self.assertShipPositionInvalid(Submarine, 'D9', Horizontal)

    def test_should_reject_addition_of_submarine_that_overflows_the_sheet_vertically(self):
        self.assertShipPositionInvalid(Submarine, 'I8', Vertical)

    def test_should_reject_addition_of_ship_at_same_location_as_existing_ship(self):
        self.rules.ship_added(AircraftCarrier('C3', Horizontal))
        self.assertShipPositionInvalid(Cruiser, 'C3', Horizontal)

    def test_should_reject_addition_of_ship_overlaping_existing_ship(self):
        self.rules.ship_added(AircraftCarrier('C3', Horizontal))
        self.assertShipPositionInvalid(Cruiser, 'C5', Horizontal)

    def test_should_reject_addition_of_ship_crossing_existing_ship(self):
        self.rules.ship_added(AircraftCarrier('C3', Horizontal))
        self.assertShipPositionInvalid(Cruiser, 'A4', Vertical)

    def assertShipPositionInvalid(self, shipClass, location, orientation):
        with self.assertRaises(Warning):
            self.rules.assert_can_add_ship(self.sheet, shipClass(location, orientation))


