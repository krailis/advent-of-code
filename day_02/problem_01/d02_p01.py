with open('d02_p01.txt') as f:
    program = list(map(int, f.read().strip().split(',')))

# Replace before running the program
program[1], program[2] = 12, 2

pos = 0
while program[pos] != 99:
    operand_1 = program[program[pos + 1]]
    operand_2 = program[program[pos + 2]]
    program[program[pos + 3]] = (operand_1 + operand_2) if program[pos] == 1 else (operand_1 * operand_2)
    pos += 4
print(program[0])
