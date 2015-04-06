from random import choice, randint
from python.gameSheet_renderer import ROW_NAMES
from python.orientation import ORIENTATIONS


def parse_location(location):
    return location[:1], int(location[1:])


def random_location():
    return "%s%s" % (choice(ROW_NAMES), randint(1, 8))


def random_orientation():
    return choice(ORIENTATIONS)

