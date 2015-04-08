from python.ships import GameOver


class GameListener():
    def __init__(self, laser_display_board):
        self.laser_display_board = laser_display_board

    def on_new_game(self, player1, player2):
        self.laser_display_board.new_game(player1, player2)

    def on_place_ship(self, player, ship):
        self.laser_display_board.place_ship(player,
                                            ship.__class__.__name__, "%s%s" % (ship.row, ship.column),
                                            ship.orientation.__name__)

    def on_fire(self, player, location, result):
        self.laser_display_board.fire(player, location, self._format_result(player, result))

    def _format_result(self, player, result):
        if isinstance(result, GameOver):
            return "Game Over - %s Wins!" % player

        return result.__class__.__name__