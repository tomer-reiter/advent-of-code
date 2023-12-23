from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_23.txt")
input = get_list_of_strings("input_puzzle_23.txt")

opposites = {
    "<": ">",
    "v": "^",
    ">": "<",
    "^": "v",
}

def traverse_to_next_crossroads(grid, start, step_one, is_p1=True):
    steps = 0
    current = start
    next_steps = [step_one]
    while len(next_steps) == 1:
        next_step = next_steps[0]
        current = add_tuples(current, DIRECTION_VECTORS[next_step])
        steps += 1
        if current[0] == len(grid) - 1:
            # Just return a dummy direction to make recursion ahead cleaner
            return steps, current, ["X"]
        next_steps = []
        for possible_step in "<>v^".replace(opposites[next_step], ""):
            r, c = add_tuples(current, DIRECTION_VECTORS[possible_step])
            allowable_spots = "." + possible_step if is_p1 else "." + "<>^v"
            if is_in_bounds(r, c, grid) and grid[r][c] in allowable_spots:
                next_steps.append(possible_step)
    return steps, current, next_steps

def get_max_steps(grid, start, step_one, vtx_info, is_p1=True, visited=None):
    if start[0] == len(grid) - 1:
        return 0
    if (start, step_one) in vtx_info:
        steps, pos, next_steps = vtx_info[(start, step_one)]
    else:
        steps, pos, next_steps = traverse_to_next_crossroads(grid, start, step_one, is_p1=is_p1)
        vtx_info[(start, step_one)] = (steps, pos, next_steps)
    if (not is_p1) and pos in visited:
        # If we've hit a dead end, we want to ignore this option
        return -10000
    new_visited = None if is_p1 else visited.union({pos})
    def get_max_steps_from_here(step):
        return get_max_steps(grid, pos, step, vtx_info, is_p1=is_p1, visited=new_visited)
    remaining_steps = list(map(get_max_steps_from_here, next_steps))
    return steps + max(remaining_steps)

# input_list: list[str]
def solve(input_list):
    vtx_info = dict()
    p1_ans = get_max_steps(input_list, (0, 1), "v", vtx_info)
    vtx_info = dict()
    p2_ans = get_max_steps(input_list, (0, 1), "v", vtx_info, is_p1=False, visited={(0, 1)})
    return p1_ans, p2_ans

# Runs in about 90 seconds on my machine
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")