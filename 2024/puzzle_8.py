from util import *
from math import gcd

def get_diff_bound(x, dx, is_lower, max_possible):
    if dx == 0:
        return -max_possible if is_lower else max_possible
    elif dx >= 0:
        return - (x // dx) if is_lower else ((max_possible - 1) - x) // dx
    else:
        return ((max_possible - 1)  - x) // dx + 1 if is_lower else -x // dx

# input_list: list[str]
def solve(input_list):
    frequencies = dict()
    n = len(input_list)
    for r in range(n):
        for c in range(n):
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
                diff = combine_tuples(c1, c2, lambda x, y: x - y)
                # Apparently this wasn't needed, at least for my input. i.e. gcd = 1 always
                # This also doesn't account for differences like (d, 0) which should  become (1, 0)
                if diff[0] != 0 and diff[1] != 0:
                    diff = (diff[0] // gcd(diff[0], diff[1]), diff[1] // gcd(diff[0], diff[1]))
                i_lower = max(combine_tuples(c1, diff, lambda x, y: get_diff_bound(x, y, True, n)))
                i_upper = min(combine_tuples(c1, diff, lambda x, y: get_diff_bound(x, y, False, n)))
                for i in range(i_lower, i_upper + 1):
                    antinodes_2.add(combine_tuples(c1, diff, lambda x, y: x + i*y))
    return len(antinodes), len(antinodes_2)

sample_input = get_list_of_strings("sample_input_puzzle_8.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_8.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")