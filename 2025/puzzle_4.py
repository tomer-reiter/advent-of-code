from util import *
from itertools import product

def remove_rolls(grid):
    removable_rolls = set()
    for p in product(range(len(grid)), range(len(grid[0]))):
        if grid[p[0]][p[1]] != "@":
            continue
        surrounding_rolls = 0
        for d in product(range(-1, 2), range(-1, 2)):
            adj = add_tuples(p, d)
            if is_in_bounds(adj[0], adj[1], grid) and grid[adj[0]][adj[1]] == "@":
                surrounding_rolls += 1
        # We count the roll itself here
        if surrounding_rolls < 5:
            removable_rolls.add(p)
    for p in removable_rolls:
        grid[p[0]][p[1]] = "."
    return len(removable_rolls)

# input_list: list[str]
def solve(input_list):
    grid = [list(row) for row in input_list]
    num_rolls_removed = [remove_rolls(grid)]
    while num_rolls_removed[-1] > 0:
        num_rolls_removed.append(remove_rolls(grid))
    return num_rolls_removed[0], sum(num_rolls_removed)

sample_input = get_list_of_strings("sample_input_puzzle_4.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_4.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")