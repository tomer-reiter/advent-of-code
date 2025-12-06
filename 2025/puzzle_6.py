from util import *
from math import prod

# input_list: list[str]
def solve(input_list):
    problems = [" ".join(row.split()).split(" ") for row in input_list]
    new_operands, operand_group = [], []
    for i in range(len(input_list[0])):
        new_operand = "".join([input_list[j][i] for j in range(len(input_list) - 1)]).replace(" ", "")
        if new_operand == "":
            new_operands.append(operand_group)
            operand_group = []
        else:
            operand_group.append(int(new_operand))
    new_operands.append(operand_group)
    grand_total_1, grand_total_2 = 0, 0
    for i in range(len(problems[-1])):
        operation = problems[-1][i]
        operands = [int(problems[j][i]) for j in range(len(problems) - 1)]
        grand_total_1 += prod(operands) if operation == "*" else sum(operands)
        grand_total_2 += prod(new_operands[i]) if operation == "*" else sum(new_operands[i])
    return grand_total_1, grand_total_2

sample_input = get_list_of_strings("sample_input_puzzle_6.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_6.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")