from unittest import TestCase
from mock import MagicMock
from python.game_listener import GameListener
from python.laser_display_board import LaserDisplayBoard
from python.orientation import Vertical
from python.ships import AircraftCarrier, Hit, GameOver


class GameListenerTest(TestCase):
    def setUp(self):
        self.mock_laser_display = MagicMock(spec=LaserDisplayBoard)

        self.listener = GameListener(self.mock_laser_display)

    def test_should_report_start_of_new_game(self):
        self.listener.on_new_game("Player1", "Player2")

        self.mock_laser_display.new_game.assert_called_once_with("Player1", "Player2")

    def test_should_report_place_ship(self):
        self.listener.on_place_ship("Player1", AircraftCarrier("F7", Vertical))

        self.mock_laser_display.place_ship.assert_called_once_with("Player1", "AircraftCarrier", "F7", "Vertical")

    def test_should_report_fire_results(self):
        self.listener.on_fire("Player1", "E3", Hit())

        self.mock_laser_display.fire.assert_called_once_with("Player1", "E3", "Hit")

    def test_should_report_end_of_game(self):
        self.listener.on_fire("Player1", "E3", GameOver())

        self.mock_laser_display.fire.assert_called_once_with("Player1", "E3", "Game Over - Player1 Wins!")
