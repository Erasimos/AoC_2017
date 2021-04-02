import ut


def get_input():
    data = [int(el) for el in ut.read_input().split()]
    return data


def get_start(banks):
    max_blocks = 0
    block_index = 0
    for index, blocks in enumerate(banks):
        if blocks > max_blocks:
            max_blocks = blocks
            block_index = index
    return block_index


def add_state(banks, states):
    new_state = "".join([str(el) + "," for el in banks])
    if states.get(new_state, False):
        return True
    else:
        states[new_state] = True


def reallocate(banks, states, cycles):

    while not add_state(banks, states):
        start_bank = get_start(banks)
        blocks = banks[start_bank]
        banks[start_bank] = 0

        # Reallocate
        index = (start_bank + 1) % len(banks)
        for i in range(blocks):
            banks[index] += 1
            index = (index + 1) % len(banks)
        cycles += 1

    return cycles


def part_one():
    banks = get_input()
    cycles = reallocate(banks, {}, 0)
    ut.print_answer(cycles)
    return


def part_two():
    banks = get_input()
    reallocate(banks, {}, 0)
    cycles = reallocate(banks, {}, 0)
    ut.print_answer(cycles)
    return


part_one()
# part_two()

