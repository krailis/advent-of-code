def run(program, noun=12, verb=2):
    # Replace before running the program
    program[1], program[2] = noun, verb
    # Get length of program

    pos = 0
    while program[pos] != 99:
        if program[pos + 1] > (len(program) - 1) or program[pos + 2] > (len(program) - 1) or \
           program[pos + 3] > (len(program) - 1):
            return None
        operand_1 = program[program[pos + 1]]
        operand_2 = program[program[pos + 2]]
        program[program[pos + 3]] = (operand_1 + operand_2) if program[pos] == 1 else (operand_1 * operand_2)
        pos += 4
    return program[0]


def find_pair_product(init_program):
    program = init_program.copy()
    for noun in range(0, 100):
        for verb in range(0, 100):
            program_output = run(program, noun, verb)
            if program_output == 19690720:
                return 100 * noun + verb
            program = init_program.copy()


if __name__ == '__main__':
    with open('../d02.txt') as f:
        initial_program = list(map(int, f.read().strip().split(',')))
    print(find_pair_product(initial_program))
