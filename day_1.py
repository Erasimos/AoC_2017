import ut


# Returns input as a list of digits
def get_input():
    data = ut.read_input()
    data = [int(el) for el in data]
    return data


# Solves part one
def part_one():
    answer = 0
    data = get_input()
    for index, digit in enumerate(data):
        next_index = (index + 1) % len(data)
        if digit == data[next_index]:
            answer += digit
    ut.print_answer(answer)


# Solves part two
def part_two():
    answer = 0
    data = get_input()
    for index, digit in enumerate(data):
        next_index = int((index + len(data)/2) % len(data))
        if digit == data[next_index]:
            answer += digit
    ut.print_answer(answer)


part_two()
# part_one()
