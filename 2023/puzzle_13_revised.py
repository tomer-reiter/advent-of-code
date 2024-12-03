from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_13.txt", "\n\n")
input = get_list_of_strings("input_puzzle_13.txt", "\n\n")

def transpose(grid):
    return ["".join(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]

# Returns the number of differing characters for two strings of equal length
def d(s_1, s_2):
    return len([k for k in range(len(s_1)) if s_1[k] != s_2[k]])

def has_horizontal_sym(grid, distance):
    rows_string = "".join(row for row in grid)
    prefix_reversed, suffix = "", rows_string
    for i in range(len(grid) - 1):
        prefix_reversed = grid[i] + prefix_reversed
        suffix = suffix[len(grid[i]):]
        common_length = min(len(prefix_reversed), len(suffix))
        if d(prefix_reversed[:common_length], suffix[:common_length]) == distance:
            return True, i + 1
    return False, 0

# input_list: list[str]
def solve(input_list):
    answers = [0, 0]
    for grid in input_list:
        for i in range(2):
            found, lines = has_horizontal_sym(grid, i)
            score = lines * 100 if found else has_horizontal_sym(transpose(grid), i)[1]
            answers[i] += score
    return answers


sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")