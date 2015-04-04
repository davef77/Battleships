from python.gameSheet import ROW_NAMES


class Horizontal():

    @classmethod
    def height(cls, waterline_length, beam):
        return beam

    @classmethod
    def width(cls, waterline_length, beam):
        return waterline_length

    @classmethod
    def place_ship(cls, position_listener, ship):
        for column in range(ship.column, ship.column + ship.waterline_length):
            position_listener.on_cell_occupied(ship.row, column - 1, ship.id)


class Vertical():

    @classmethod
    def height(cls, waterline_length, beam):
        return waterline_length

    @classmethod
    def width(cls, waterline_length, beam):
        return beam

    @classmethod
    def place_ship(cls, position_listener, ship):
        ship_row = ROW_NAMES.index(ship.row)
        for row in ROW_NAMES[ship_row:ship_row + ship.waterline_length]:
            position_listener.on_cell_occupied(row, ship.column - 1, ship)

