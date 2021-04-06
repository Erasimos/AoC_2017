import ut


def get_input():
    data = [line.split(" <-> ") for line in ut.read_input().splitlines()]
    programs = {}
    for el in data:
        programs[el[0]] = el[1].split(", ")
    return programs


puzzle_input = get_input()


def find_connected(programs, program_id, group):
    for neighbour in programs[program_id]:
        if neighbour not in group:
            group.append(neighbour)
            find_connected(programs, neighbour, group)
    return group


def find_groups(programs):
    removed = []
    groups = 0
    for program_id in range(0, len(programs)):
        program_id = str(program_id)
        if program_id not in removed:
            group = find_connected(programs, program_id, [])
            removed.extend(group)
            groups += 1
    return groups


def part_one():
    group = find_connected(puzzle_input, '0', [])
    ut.print_answer(len(group))
    return


def part_two():
    groups = find_groups(puzzle_input)
    ut.print_answer(groups)
    return


# part_one()
part_two()

