from util import *

# The mazes are just a straight path from start to end, so we don't care where the start is
def find_end(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "E":
                return r, c

def find_distances(grid, end):
    distances = {end: 0}
    boundary = {end}
    dist = 0
    while len(boundary) != 0:
        new_boundary = set()
        dist += 1
        for p in boundary:
            for d in "^>v<":
                new_p = add_tuples(p, DIRECTION_VECTORS[d])
                if grid[new_p[0]][new_p[1]] != "#" and new_p not in distances:
                    distances[new_p] = dist
                    new_boundary.add(new_p)
        boundary = new_boundary
    return distances

def count_shortcuts(distances, cheat_time, min_saved):
    count = 0
    for p in distances:
        for ew in range(-cheat_time, cheat_time + 1):
            for ns in range(-cheat_time + abs(ew), cheat_time + 1 - abs(ew)):
                new_p = add_tuples(p, (ew, ns))
                time_saved = distances[p] - distances.get(new_p, distances[p]) - abs(ew) - abs(ns)
                count += 1 if time_saved >= min_saved else 0
    return count

# input_list: list[str]
def solve(input_list, min_saved_1, min_saved_2):
    end = find_end(input_list)
    distances = find_distances(input_list, end)
    return count_shortcuts(distances, 2, min_saved_1), count_shortcuts(distances, 20, min_saved_2)

# Runs in about 4 seconds on my machine
sample_input = get_list_of_strings("sample_input_puzzle_20.txt")
sample_p1, sample_p2 = solve(sample_input, 2, 50)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_20.txt")
p1, p2 = solve(input, 100, 100)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")