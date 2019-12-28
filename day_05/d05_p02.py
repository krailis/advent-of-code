def parse_code(code):
    code = str(code)
    code = code.zfill(5)
    digits = list(code)
    op_code = int("".join(digits[-2:]))
    third, second, first = map(int, digits[0:3])
    return op_code, first, second, third


def run_program(program):
    pos = 0
    while program[pos] != 99:
        op_code, first, second, _ = parse_code(program[pos])
        if op_code == 3:
            num = int(input())
            program[program[pos + 1]] = num
            pos += 2
        elif op_code == 4:
            operand = program[program[pos + 1]] if first == 0 else program[pos + 1]
            print(operand)
            pos += 2
        else:
            operand_1 = program[program[pos + 1]] if first == 0 else program[pos + 1]
            operand_2 = program[program[pos + 2]] if second == 0 else program[pos + 2]
            if op_code == 5:
                pos = operand_2 if operand_1 != 0 else (pos + 3)
            elif op_code == 6:
                pos = operand_2 if operand_1 == 0 else (pos + 3)
            elif op_code == 7:
                program[program[pos + 3]] = 1 if operand_1 < operand_2 else 0
                pos += 4
            elif op_code == 8:
                program[program[pos + 3]] = 1 if operand_1 == operand_2 else 0
                pos += 4
            else:
                program[program[pos + 3]] = (operand_1 + operand_2) if op_code == 1 else (operand_1 * operand_2)
                pos += 4


with open('d05.txt') as f:
    initial_program = list(map(int, f.read().strip().split(',')))
run_program(initial_program)
