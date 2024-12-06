from util import *

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

def get_path(grid, pos_and_dir):
    visited_pos, visited = {pos_and_dir[0]}, {pos_and_dir}
    while(True):
        next_pos = add_tuples(pos_and_dir[0], DIRECTION_VECTORS[pos_and_dir[1]])
        if not is_in_bounds(*next_pos, grid):
            return visited_pos
        elif grid[next_pos[0]][next_pos[1]] == "#":
            pos_and_dir = pos_and_dir[0], turn_right[pos_and_dir[1]]
        else:
            visited_pos.add(next_pos)
            pos_and_dir = next_pos, pos_and_dir[1]
        if pos_and_dir in visited:
            return -1
        visited.add(pos_and_dir)

# input_list: list[str]
def solve(input_list):
    start = find_start(input_list), "^"
    uninterrupted = get_path(input_list, start)
    p2 = 0
    for r, c in uninterrupted:
        new_grid = input_list.copy()
        new_grid[r] = new_grid[r][:c] + "#" + new_grid[r][c + 1:]
        if get_path(new_grid, start) == -1:
            p2 += 1
    return len(uninterrupted), p2

# Runs in about 13 seconds on my machine
sample_input = get_list_of_strings("sample_input_puzzle_6.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_6.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")