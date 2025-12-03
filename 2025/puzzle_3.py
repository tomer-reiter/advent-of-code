from util import *

def find_joltage(bank, digits):
    i, joltage = 0, ""
    for d in range(digits):
        next_battery = max(bank[i:-(digits - 1 - d)]) if d < digits - 1 else max(bank[i:])
        joltage += next_battery
        i = bank[i:].find(next_battery) + i + 1
    return int(joltage)

# input_list: list[str]
def solve(input_list):
    return (sum(map(lambda b: find_joltage(b, digits), input_list)) for digits in [2, 12])

sample_input = get_list_of_strings("sample_input_puzzle_3.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_3.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")