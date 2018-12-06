"""SOLID. LSP"""


class Rectangle(object):

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


class Square(Rectangle):
    def set_width(self, width):
        super(Square, self).set_height(width)
        super(Square, self).set_width(width)

    def set_height(self, height):
        super(Square, self).set_height(height)
        super(Square, self).set_width(height)


def calculate_square(rec, width, height):
    rec.set_width(width)
    rec.set_height(height)
    print(rec.width * rec.height)


calculate_square(Rectangle(), 4, 5)  # 20
calculate_square(Square(), 4, 5)     # 25 ???
