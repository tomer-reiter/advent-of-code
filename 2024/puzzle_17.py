from util import *

def combo_op(op, registers):
    return op if op <= 3 else registers[op - 4]

def perform_instruction(inst, op, registers, output, inst_index):
    next_index = 2 + inst_index
    if inst == 0:
        registers[0] //= 2 ** combo_op(op, registers)
    elif inst == 1:
        registers[1] = registers[1] ^ op
    elif inst == 2:
        registers[1] = combo_op(op, registers) % 8
    elif inst == 3 and registers[0] != 0:
        next_index = op
    elif inst == 4:
        registers[1] = registers[1] ^ registers[2]
    elif inst == 5:
        output += [combo_op(op, registers) % 8]
    elif inst == 6:
        registers[1] = registers[0] // 2 ** combo_op(op, registers)
    elif inst == 7:
        registers[2] = registers[0] // 2 ** combo_op(op, registers)
    return next_index

def get_output(registers, instructions):
    current_inst = 0
    outputs = []
    while current_inst < len(instructions) - 1:
        current_inst = perform_instruction(
            instructions[current_inst],
            instructions[current_inst + 1],
            registers,
            outputs,
            current_inst
        )
    return outputs

# input_list: list[str]
def solve(input_list):
    registers = [int(s[s.find(": ") + 2:]) for s in input_list[0]]
    instructions = input_list[1][0][input_list[1][0].find(": ") + 2:]
    instructions = [int(i) for i in instructions.split(",")]
    # If you read the program for my input, the output only ever depends on the last
    # 10 binary digits of A, then it divides A by 8, and repeats. So we find the set of possible
    # ending 10 binary digits, then the set of possible digits 4-13, compare those against what
    # we have so far to find the set of possible ending 13 digits, and repeat
    # This works for the sample too, although it's overkill for that case
    first_outputs = {i: [] for i in range(1024)}
    for i in range(2 ** 10):
        first_outputs[get_output([i, 0, 0], instructions)[0]] += [i]
    possible_As = set(first_outputs[instructions[0]])
    for i in range(1, len(instructions)):
        inst = instructions[i]
        next_As = set()
        for n in first_outputs[inst]:
            for m in possible_As:
                if n % (2 ** 7) == m // 2 ** (3 * i):
                    next_As.add(n * (2 ** (3 * i)) + m % (2 ** (3 * i)))
        possible_As = next_As
    return ",".join([str(n) for n in get_output(registers, instructions)]), min(possible_As)

sample_input = get_list_of_strings("sample_input_puzzle_17.txt", line_break="\n\n")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_17.txt", line_break="\n\n")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")