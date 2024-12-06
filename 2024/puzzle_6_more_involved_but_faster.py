from util import *
# While this file runs faster, I haven't cleaned it up so it's likely harder to read

turn_right = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}

def find_start(grid):
    for r in range(len(grid)):
        # By inspection, actual input has ^ as start as well
        if "^" in grid[r]:
            return (r, grid[r].index("^"))

def get_path(grid, pos, visited_with_dirs = dict()):
    visited = {pos[0]}
    while(True):
        next_pos = add_tuples(pos[0], DIRECTION_VECTORS[pos[1]])
        if not is_in_bounds(*next_pos, grid):
            return visited, visited_with_dirs
        elif grid[next_pos[0]][next_pos[1]] == "#":
            new_pos = pos[0], turn_right[pos[1]]
        else:
            visited.add(next_pos)
            new_pos = next_pos, pos[1]
        if new_pos in visited_with_dirs:
            return -1
        visited_with_dirs[pos] = new_pos
        pos = new_pos

# input_list: list[str]
def solve(input_list):
    start_pos = find_start(input_list), "^"
    pos = start_pos
    uninterrupted, uninterrupted_with_dirs = get_path(input_list, pos)
    p2 = 0
    visited_with_dirs = dict()
    while pos in uninterrupted_with_dirs:
        (r, c), d = pos
        next_pos = uninterrupted_with_dirs[pos]
        (next_r, next_c), next_d = next_pos
        visited_with_dirs[((r, c), d)] = ((next_r, next_c), next_d)
        if next_pos == start_pos or (next_r == r and next_c == c):
            pos = next_pos
            continue
        new_grid = input_list.copy()
        new_grid[next_r] = new_grid[next_r][:next_c] + "#" + new_grid[next_r][next_c + 1:]
        if get_path(new_grid, ((r, c), d), visited_with_dirs.copy()) == -1:
            p2 += 1
        pos = next_pos
    return len(uninterrupted), p2

# Runs in under 3 seconds on my machine
sample_input = get_list_of_strings("sample_input_puzzle_6.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_6.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")