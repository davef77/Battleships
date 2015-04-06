MAX_COLUMNS = 8
MAX_ROWS = 8

ROW_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


class GameSheetRenderer():

    def render_sheet(self, sheet):
        sheet_str = ""
        for row in ROW_NAMES:
            sheet_str = self._render_row(sheet, row, sheet_str)
        sheet_str += self._footer()
        return sheet_str

    def _render_row(self, sheet, row, sheet_str):
        sheet_str += row

        for column in range(0, MAX_COLUMNS):
            sheet_str += self._render_cell(sheet, row, column)

        sheet_str += '\n'

        return sheet_str

    def _footer(self):
        footer = '.'

        for column in range(0, MAX_COLUMNS):
            footer += str(column + 1)

        return footer


class DefenseSheetRenderer(GameSheetRenderer):

    def _render_cell(self, sheet, row, column):
        return sheet[row][column]


class HitAndMissesSheetRenderer(GameSheetRenderer):

    def _render_cell(self, sheet, row, column):
        value = sheet[row][column]
        if value in ['A', 'B', 'C', 'D', 'S']:
            return '.'
        return value


