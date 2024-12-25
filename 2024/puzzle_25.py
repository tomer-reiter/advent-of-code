from util import *
from itertools import product

def parse_input(locks_and_keys):
    locks, keys = [], []
    for object in locks_and_keys:
        heights = [0] * len(object[0])
        for r, c in product(range(len(object)), range(len(object[0]))):
            heights[c] += 1 if object[r][c] == "#" else 0
        if object[0][0] == "#":
            keys += [heights]
        else:
            locks += [heights]
    return locks, keys

# input_list: list[str]
def solve(input_list):
    locks, keys = parse_input(input_list)
    max_height = len(input_list[0])
    total = 0
    for lock, key in product(locks, keys):
        totals = add_tuples(lock, key)
        total += 1 if all(col_height <= max_height for col_height in totals) else 0
    return total

sample_input = get_list_of_strings("sample_input_puzzle_25.txt", line_break="\n\n")
print(f"Part 1 answer for sample input: {solve(sample_input)}")

input = get_list_of_strings("input_puzzle_25.txt", line_break="\n\n")
print(f"Part 1 final answer: {solve(input)}")