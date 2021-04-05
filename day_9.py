import ut


def get_input():
    data = ut.read_input()
    return data


puzzle_input = get_input()


def count_score():
    score = 0
    in_garbage = False
    depth = 0
    index = 0
    while index < len(puzzle_input):

        char = puzzle_input[index]

        if char == '!':
            index += 1

        elif in_garbage and char == '>':
            in_garbage = False

        elif not in_garbage:
            if char == '<':
                in_garbage = True
            elif char == '{':
                depth += 1
            elif char == '}':
                score += depth
                depth -= 1
        index += 1
    return score


def count_garbage():
    garbage = 0
    in_garbage = False
    index = 0
    while index < len(puzzle_input):

        char = puzzle_input[index]

        if char == '!':
            index += 1

        elif in_garbage and char == '>':
            in_garbage = False
        elif in_garbage:
            garbage += 1

        elif not in_garbage:
            if char == '<':
                in_garbage = True

        index += 1
    return garbage


def part_one():
    ut.print_answer(count_score())
    return


def part_two():
    ut.print_answer(count_garbage())
    return


#part_one()
part_two()

