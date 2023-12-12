from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_12.txt")
input = get_list_of_strings("input_puzzle_12.txt")

def is_compatible(arrangement, options):
    for i in range(len(arrangement)):
        if options[i] != "?" and options[i] != arrangement[i]:
            return False
    return True

def count_possibilities(row, clues, answers):
    if (row, clues) in answers:
        return answers[(row, clues)]
    if len(clues) == 0:
        return 0 if "#" in row else 1
    total_possibilities = 0
    length = clues[0]
    block = "#" * length + "."
    for i in range(len(row) - length):
        if is_compatible(block, row[i:]):
            remaining = row[i + length + 1:]
            total_possibilities += count_possibilities(remaining, clues[1:], answers)
        if row[i] == "#":
            # We need to place a block by the time we see the first #
            break
    answers[(row, clues)] = total_possibilities
    return total_possibilities

# input_list: list[str]
def solve(input_list):
    p1 = 0
    p2 = 0
    for line in input_list:
        row, clues = line.split()
        # Having a dot at the end helps simplify the recursive algorithm above:
        # we avoid index issues when placing blocks like ###. at the end
        p1_row = row if row[-1] == "." else row + "."
        p2_row = ((row + "?") * 5)[:-1] + "."
        clues = tuple(map(lambda x: int(x), clues.split(",")))
        p2_clues = clues * 5
        p1 += count_possibilities(p1_row, clues, dict())
        p2 += count_possibilities(p2_row, p2_clues, dict())
    return p1, p2

# Runs in about 1.35 seconds on my machine
sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")