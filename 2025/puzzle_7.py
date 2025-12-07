from util import *

# input_list: list[str]
def solve(input_list):
    beam_cols = {input_list[0].find("S"): 1}
    total_splits = 0
    for r in range(1, len(input_list)):
        new_beams = dict()
        for c, n in beam_cols.items():
            if input_list[r][c] == "^":
                new_beams[c - 1] = new_beams.get(c - 1, 0) + n
                new_beams[c + 1] = new_beams.get(c + 1, 0) + n
                total_splits += 1
            else:
                new_beams[c] = new_beams.get(c, 0) + n
        beam_cols = new_beams
    return total_splits, sum(beam_cols.values())

sample_input = get_list_of_strings("sample_input_puzzle_7.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_7.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")