from util import *

def trailhead_score(grid, trailhead):
    reachable = {i: set([trailhead]) if i == 0 else set() for i in range(10)}
    path_count = {trailhead: 1}
    for i in range(1, 10):
        for coord in reachable[i - 1]:
            for d in "NESW":
                new_coord = add_tuples(coord, DIRECTION_VECTORS[d])
                if is_in_bounds(*new_coord, grid) and grid[new_coord[0]][new_coord[1]] == i:
                    reachable[i].add(new_coord)
                    path_count[new_coord] = path_count.get(new_coord, 0) + path_count[coord]
    return len(reachable[9]), sum([path_count[coord] for coord in reachable[9]])

# input_list: list[str]
def solve(input_list):
    grid = [[int(c) for c in line] for line in input_list]
    p1, p2 = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                p1, p2 = add_tuples((p1, p2), trailhead_score(grid, (r, c)))
    return p1, p2

sample_input = get_list_of_strings("sample_input_puzzle_10.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_10.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")