class Horizontal():

    @classmethod
    def height(cls, waterline_length, beam):
        return beam

    @classmethod
    def width(cls, waterline_length, beam):
        return waterline_length


class Vertical():

    @classmethod
    def height(cls, waterline_length, beam):
        return waterline_length

    @classmethod
    def width(cls, waterline_length, beam):
        return beam

