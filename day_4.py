import ut


def get_input():
    data = ut.read_input().splitlines()
    return data


puzzle_input = get_input()


def is_valid(phrase):
    phrase_dict = {}
    for word in phrase.split():
        if phrase_dict.get(word, False):
            return False
        else:
            phrase_dict[word] = True
    return True


def is_valid2(phrase):
    phrase_dict = {}
    for word in phrase.split():
        word = "".join(sorted(word))
        if phrase_dict.get(word, False):
            return False
        else:
            phrase_dict[word] = True
    return True


def part_one():
    valid_count = 0
    for phrase in puzzle_input:
        if is_valid(phrase):
            valid_count += 1
    ut.print_answer(valid_count)


def part_two():
    valid_count = 0
    for phrase in puzzle_input:
        if is_valid2(phrase):
            valid_count += 1
    ut.print_answer(valid_count)


# part_one()
part_two()

