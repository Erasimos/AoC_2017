import ut


def get_input():
    data = [line.split() for line in ut.read_input().splitlines()]
    return data


puzzle_input = get_input()


class Computer:

    def __init__(self):
        self.registers = {}
        self.max_value = 0

    def do_instruction(self, instruction):
        target_reg = instruction[0]
        other_reg = instruction[4]
        condition = instruction[5]
        condition_val = instruction[6]
        val_to_add = int(instruction[2]) if instruction[1] == "inc" else -int(instruction[2])
        modify = eval(str(self.registers.get(other_reg, 0)) + condition + condition_val)
        if modify:
            self.registers[target_reg] = self.registers.get(target_reg, 0) + val_to_add

        self.max_value = max(self.max_value, self.registers.get(target_reg, 0))

    def run(self, instructions):
        for instruction in instructions:
            self.do_instruction(instruction)


def part_one():
    computer = Computer()
    computer.run(puzzle_input)
    answer = max(computer.registers.values())
    ut.print_answer(answer)
    return


def part_two():
    computer = Computer()
    computer.run(puzzle_input)
    ut.print_answer(computer.max_value)
    return


#part_one()
part_two()

