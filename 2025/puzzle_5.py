from util import *

def solve(input_list):
    ing_ranges = sorted([(int(s.split("-")[0]), int(s.split("-")[1])) for s in input_list[0]])
    total = 0
    for ingredient in input_list[1]:
        total += any([low <= int(ingredient) <= high for low, high in ing_ranges])
    # This code for part 2 below effectively creates an ordered list of non-overlapping ranges.
    # This could be used for part 1 with a binary search, but brute force is already < 0.02s 
    total_in_ranges, highest = 0, 0
    for low, high in ing_ranges:
        total_in_ranges += max(high, highest) - max(low, highest + 1) + 1
        highest = max(highest, high)
    return total, total_in_ranges

sample_input = get_list_of_strings("sample_input_puzzle_5.txt", line_break="\n\n")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_5.txt", line_break="\n\n")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")