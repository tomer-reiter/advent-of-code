from util import *

def is_safe(line):
    diffs = [int(line[i+1]) - int(line[i]) for i in range(len(line) - 1)]
    in_range = [-3 <= d <= 3 for d in diffs]
    signs = {d/abs(d) if d != 0 else 0 for d in diffs}
    return len(signs) == 1 and 0 not in signs and all(in_range)

def is_safe_with_removal(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        if is_safe(line[:i] + line[i + 1:]):
            return True
    return False

# input_list: list[str]
def solve(input_list):
    safe_list = [is_safe(line) for line in input_list]
    safe_with_removal_list = [is_safe_with_removal(line) for line in input_list]
    return safe_list.count(True), safe_with_removal_list.count(True)

sample_input = get_list_of_strings("sample_input_puzzle_2.txt", separation=" ")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_2.txt", separation=" ")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")