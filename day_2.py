import ut
import math


def get_input():
    data = ut.read_input()
    data = data.splitlines()
    data = [el.split() for el in data]
    data = [[int(val) for val in row] for row in data]
    return data


def part_one():
    data = get_input()
    checksum = 0
    for row in data:
        min_val = math.inf
        max_val = 0
        for val in row:
            min_val = min(min_val, val)
            max_val = max(max_val, val)
        checksum += (max_val - min_val)
    ut.print_answer(checksum)
    return


def part_two():
    data = get_input()
    checksum = 0
    for row in data:
        match = False
        for index, val in enumerate(row):
            for next_val in row[(index + 1):]:
                if max(val, next_val) % min(val, next_val) == 0:
                    checksum += max(val, next_val) / min(val, next_val)
                    match = True
                    break
            if match:
                break
    ut.print_answer(checksum)
    return


# part_one()
part_two()

