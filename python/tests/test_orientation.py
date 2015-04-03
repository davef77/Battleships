from unittest import TestCase
from python.orientation import Vertical, Horizontal

WATERLINE_LENGTH = 5
BEAM = 1


class VerticalTest(TestCase):

    def test_should_return_beam_for_width(self):
        self.assertEquals(BEAM, Vertical.width(WATERLINE_LENGTH, BEAM))

    def test_should_return_waterline_length_for_height(self):
        self.assertEquals(WATERLINE_LENGTH, Vertical.height(WATERLINE_LENGTH, BEAM))


class HorizontalTest(TestCase):

    def test_should_return_waterline_length_for_width(self):
        self.assertEquals(WATERLINE_LENGTH, Horizontal.width(WATERLINE_LENGTH, BEAM))

    def test_should_return_beam_for_height(self):
        self.assertEquals(BEAM, Horizontal.height(WATERLINE_LENGTH, BEAM))


