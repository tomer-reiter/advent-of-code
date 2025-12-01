from util import *

# input_list: list[str]
# This approach uses modular arithmetic but requires some correction for left
# turns that start or end at 0
def solve(input_list):
    dial_pos, password, password_2 = 50, 0, 0
    for instruction in input_list:
        d, n = instruction[0], int(instruction[1:])
        password_2 -= dial_pos == 0 and d == "L"
        dial_pos += n if d == "R" else -n
        password_2 += abs(dial_pos // 100)
        dial_pos %= 100
        password += dial_pos == 0
        password_2 += dial_pos == 0 and d == "L"
    return password, password_2

# This approach is more brute force but doesn't require any special cases
def solve_alt(input_list):
    dial_pos, password, password_2 = 50, 0, 0
    for instruction in input_list:
        d, n = instruction[0], int(instruction[1:])
        for _ in range(n):
            dial_pos += 1 if d == "R" else -1
            password_2 += dial_pos % 100 == 0
        password += dial_pos % 100 == 0
    return password, password_2

sample_input = get_list_of_strings("sample_input_puzzle_1.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_1.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")