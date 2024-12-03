from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_17.txt")
input = get_list_of_strings("input_puzzle_17.txt")

opposite_directions = {
    "NS": "EW",
    "EW": "NS",
}

# This an implementation of Dijkstra's algorithm. Instead of storing a graph,
# it's stored implicitly via the grid. Vertices are of the form i, j, directions,
# where i, j are the coordinates in the grid and directions contain the way we
# entered that vertex (so then we have to turn next)
def find_min_path(grid, min_move, max_move):
    distances = dict()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            distances[(i, j, "NS")] = 1000000
            distances[(i, j, "EW")] = 1000000
    distances[(0, 0, "EW")] = 0
    distances[(0, 0, "NS")] = 0
    visited = set()
    seen = set(distances.keys())
    target_r, target_c = len(grid) - 1, len(grid[0]) - 1
    target_1, target_2 = (target_r, target_c, "NS"), (target_r, target_c, "EW")
    while not (target_1 in visited and target_2 in visited):
        r, c, d_old = min([x for x in seen if not x in visited], key=(lambda x: distances[x]))
        other_directions = opposite_directions[d_old]
        for d in other_directions:
            for n in range(min_move, max_move + 1):
                this_path_value = 0
                new_r, new_c = r, c
                for i in range(n):
                    new_r, new_c = add_tuples((new_r, new_c), DIRECTION_VECTORS[d])
                    if is_in_bounds(new_r, new_c, grid):
                        this_path_value += int(grid[new_r][new_c])
                if is_in_bounds(new_r, new_c, grid):
                    new_spot = (new_r, new_c, other_directions)
                    seen.add(new_spot)
                    distances[new_spot] = min(distances[new_spot], this_path_value + distances[(r, c, d_old)])
        visited.add((r, c, d_old))
        seen.remove((r, c, d_old))
    return min(distances[target_1], distances[target_2])

# input_list: list[str]
def solve(input_list):
    return find_min_path(input_list, 1, 3), find_min_path(input_list, 4, 10)

# Runs in under 8 minutes on my machine
sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")