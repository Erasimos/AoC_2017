import ut


def get_input():
    data = ut.read_input().split(",")
    return data


puzzle_input = get_input()


class HexGrid:

    def __init__(self):
        self.pos = (0, 0)
        self.delta_step = \
        {
            'n' : (0, 1),
            'ne': (0.5, 0.5),
            'se': (0.5, -0.5),
            's': (0, -1),
            'sw': (-0.5, -0.5),
            'nw': (-0.5, 0.5),
        }
        self.max_dist = 0

    def hex_walk(self, directions):
        for direction in directions:
            delta_move = self.delta_step[direction]
            self.pos = (self.pos[0] + delta_move[0], self.pos[1] + delta_move[1])
            dist = abs(self.pos[0]) + abs(self.pos[1])
            self.max_dist = max(self.max_dist, dist)


def part_one():

    hex_grid = HexGrid()
    hex_grid.hex_walk(puzzle_input)
    ut.print_answer(hex_grid.pos)
    return


def part_two():
    hex_grid = HexGrid()
    hex_grid.hex_walk(puzzle_input)
    ut.print_answer(hex_grid.max_dist)
    return


#part_one()
part_two()

