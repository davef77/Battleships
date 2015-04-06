from python.gameSheet import GameSheet
from python.rules import Rules


class GameSheetFactory():
    def create_game_sheet(self):
        return GameSheet(Rules())

