

class BattleShips(object):

    def __init__(self, game_sheet_factory):
        self.game_sheet_factory = game_sheet_factory

    def new_game(self):
        self.game_sheet_factory.create_game_sheet()



