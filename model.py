import board

l_positions = [
    [(0, 1), (1, 1), (2, 1), (2, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(2, 1), (1, 1), (0, 1), (0, 0)],
    [(1, 2), (1, 1), (1, 0), (2, 0)]
]

class Piece(object):

    def __init__(self, character, positions):
        self.character = character
        self.positions = positions
        self.current_position = 0

    def rotate_right(self):
        self.current_position += 1
        if self.current_position == len(self.positions):
            self.current_position = 0

    def rotate_left(self):
        self.current_position -= 1
        if self.current_position < 0:
            self.current_position = len(self.positions) - 1

    def position(self):
        return self.positions[self.current_position]

class TetrisBoard(board.Board):

    def place_piece(self, piece, starting_coord):
        sx, sy = starting_coord
        coords = [(x + sx, y + sy) for (x, y) in piece]
        for coord in coords:
            self[coord] = "*"


if __name__ == '__main__':
    b = TetrisBoard((8, 8))
    l_shape = Piece("*", l_positions)

    b.place_piece(l_shape.position(), (0, 0))
    b.draw()
    input("Enter...")
    b.clear()
    l_shape.rotate_right()
    b.place_piece(l_shape.position(), (0, 0))
    b.draw()
    input("Enter...")
    b.clear()
    l_shape.rotate_left()
    b.place_piece(l_shape.position(), (0, 0))
    b.draw()
