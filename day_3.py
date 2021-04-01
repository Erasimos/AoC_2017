import ut


def get_input():
    data = int(ut.read_input())
    return data


puzzle_input = get_input()


class MemoryWriter:
    def __init__(self, end):
        self.memory = {(0, 0): 1}
        self.x = 0
        self.y = 0
        self.val = 1
        self.end = end

    def step(self, dx, dy):
        self.x += dx
        self.y += dy

        mem_sum = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                mem_sum += self.memory.get((self.x + x, self.y + y), 0)

        self.memory[(self.x, self.y)] = mem_sum
        self.val = mem_sum
        print(self.val)

    def write(self, n, e, s, w):

        # Step east
        self.step(1, 0)
        if self.val >= self.end:
            return self.x, self.y

        # Go north
        for i in range(n):
            self.step(0, 1)
            if self.val >= self.end:
                return self.x, self.y
        # Go west
        for i in range(w):
            self.step(-1, 0)
            if self.val >= self.end:
                return self.x, self.y
        # Go south
        for i in range(s):
            self.step(0, -1)
            if self.val >= self.end:
                return self.x, self.y
        # Go east
        for i in range(e):
            self.step(1, 0)
            if self.val >= self.end:
                return self.x, self.y

        return self.write(n + 2, e + 2, s + 2, w + 2)

    def start(self):
        return self.write(1, 2, 2, 2)


def part_one():

    memory_writer = MemoryWriter(347991)
    x, y = memory_writer.start()
    answer = abs(x) + abs(y)
    ut.print_answer(answer)

    return


def part_two():
    memory_writer = MemoryWriter(347991)
    x, y = memory_writer.start()
    return


# part_one()
part_two()

