from util import *

# input_list: list[str]
def solve(input_list):
    frequencies = dict()
    for r in range(len(input_list)):
        for c in range(len(input_list[0])):
            if input_list[r][c] != ".":
                frequencies[input_list[r][c]] = frequencies.get(input_list[r][c], []) + [(r, c)]
    antinodes, antinodes_2 = set(), set()
    for coords in frequencies.values():
        for c1 in coords:
            for c2 in coords:
                if c1 == c2:
                    continue
                antinode = combine_tuples(c1, c2, lambda x, y: 2 * x - y)
                if is_in_bounds(*antinode, input_list):
                    antinodes.add(antinode)
                i = 0
                while is_in_bounds(
                    *combine_tuples(c1, c2, lambda x, y: (1 + i) * x - i * y), input_list
                ):
                    antinodes_2.add(combine_tuples(c1, c2, lambda x, y: (1 + i) * x - i * y))
                    i += 1
    return len(antinodes), len(antinodes_2)

sample_input = get_list_of_strings("sample_input_puzzle_8.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_8.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")