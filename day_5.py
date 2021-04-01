import ut


def get_input():
    data = [int(el) for el in ut.read_input().splitlines()]
    return data


puzzle_input = get_input()


def execute():
    instructions = puzzle_input
    index = 0
    steps = 0
    while 0 <= index < len(instructions):
        new_index = index + instructions[index]
        instructions[index] += 1
        index = new_index
        steps += 1
    return steps


def execute2():
    instructions = puzzle_input
    index = 0
    steps = 0
    while 0 <= index < len(instructions):
        new_index = index + instructions[index]

        if instructions[index] >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1

        index = new_index
        steps += 1
    return steps


def part_one():
    ut.print_answer(execute())


def part_two():
    ut.print_answer(execute2())
    return


# part_one()
part_two()

