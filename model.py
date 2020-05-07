import board

l_orientations = [
    [(0, 1), (1, 1), (2, 1), (2, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(2, 1), (1, 1), (0, 1), (0, 0)],
    [(1, 2), (1, 1), (1, 0), (2, 0)]
]

i_orientations = [
    [(0, 1), (1, 1), (2, 1), (3, 1)],
    [(1, 0), (1, 1), (1, 2), (1, 3)]
]

sq_orientations = [[(0, 1), (1, 1), (1, 0), (0, 0)]]

three_orientations = [
    [(0, 1), (1, 1), (2, 1), (1, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(1, 1), (1, 1), (0, 1), (0, 0)],
    [(1, 2), (1, 1), (1, 0), (1, 0)]
]

z_orientations = [
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(2, 0), (1, 1), (2, 1), (1, 2)]
]


s_orientations = [
    [(2, 0), (0, 1), (1, 1), (1, 0)],
    [(1, 0), (1, 1), (2, 1), (2, 2)]
]

rl_orientations = [
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(1, 0), (1, 1), (1, 2), (2, 0)],
    [(2, 1), (1, 1), (0, 1), (0, 0)],
    [(1, 2), (1, 1), (1, 0), (0, 2)]
]

#
# Current Coord is the top-left corner of the bounding box
# That way, we can check what happens if we drop the entire
# box down by one (or left or whatever) and see if it fits
#

class Piece(object):

    def __init__(self, character, orientations, initial_coord, game_board):
        self.character = character
        self.orientations = orientations
        self.current_orientation = 0
        self.current_coord = initial_coord
        self.game_board = game_board

    def __iter__(self):
        return self.orientations[self.current_orientation]

    def rotate_right(self):
        self.current_orientation += 1
        if self.current_orientation == len(self.orientations):
            self.current_orientation = 0

    def rotate_left(self):
        self.current_orientation -= 1
        if self.current_orientation < 0:
            self.current_orientation = len(self.orientations) - 1

    def move(self, vector):
        x, y = self.current_coord
        dx, dy = vector
        self.current_coord = (x + dx, y + dy)

    def move_left(self):
        x, y = self.current_coord
        self.current_coord = (x  - 1,  y)

    def move_right(self):
        x, y = self.current_coord
        self.current_coord = (x + 1,  y)

    def orientation(self):
        return self.orientations[self.current_orientation]

    def board_coords(self):
        return self.coords_offset_by(self.orientation, self.current_coord)

    def coord_offset_by(self, coord, vector):
        x, y = coord
        dx, dy = vector
        return (x + dx, y + dy)

    def coords_offset_by(self, coords, vector):
        return [self.coord_offset_by(coord, vector) for c in coords]

    def repositioned(self, vector):
        return self.coords_offset_by(self.orientations(), vector)

    def can_drop(self):
        new_orientation = self.coords_offset_by(self.repositioned((0, 1)), self.current_coord)
        if any(self.game_board[coord] for coord in new_orientation):
            return False

    def can_go_left(self):
        new_orientation = self.coords_offset_by(self.repositioned((-1, 0)), self.current_coord)
        if any(self.game_board[coord] for coord in new_orientation):
            return False
        if any(coord not in self.game_board for coord in new_orientation):
            return False

    def can_go_right(self):
        new_orientation = self.coords_offset_by(self.repositioned((+1, 0)), self.current_coord)
        if any(self.game_board[coord] for coord in new_orientation):
            return False
        if any(coord not in self.game_board for coord in new_orientation):
            return False

class TetrisBoard(board.Board):

    def move_piece(self, piece, vector):
        for coord in piece.board_coords:
            del self[coord]
        piece.move(vector)
        for coord in piece.board_coords:
            self[coord] = piece.character


b = TetrisBoard((10, 20))

l_shape = Piece("*", l_orientations, (0, 0), b)
three_shape = Piece("+", three_orientations, (0, 0), b)

