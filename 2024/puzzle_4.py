from util import *

# input_list: list[str]
def solve(input_list):
    dirs = [(1, 0), (0, 1), (1, 1), (-1, 1)]
    xmases, xdashes = 0, 0
    for r in range(len(input_list)):
        for c in range(len(input_list[0])):
            for (rd, cd) in dirs:
                if (is_in_bounds(r + 3*rd, c + 3*cd, input_list)
                    and "".join([input_list[r + i*rd][c + i*cd] for i in range(4)]) in {"XMAS", "SAMX"}):
                    xmases += 1
            if (is_in_bounds(r + 1, c + 1, input_list) and is_in_bounds(r - 1, c - 1, input_list)
                and "".join([input_list[r + i][c + i] for i in range(-1, 2)]) in {"SAM", "MAS"}
                and "".join([input_list[r + i][c - i] for i in range(-1, 2)]) in {"SAM", "MAS"}):
                xdashes += 1
    return xmases, xdashes

sample_input = get_list_of_strings("sample_input_puzzle_4.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_4.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")