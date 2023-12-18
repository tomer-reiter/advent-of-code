from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_18.txt")
input = get_list_of_strings("input_puzzle_18.txt")

# Returns row intervals where in each interval, all rows are the same
def get_row_intervals(instructions):
    endpoints = set()
    r, c = 0, 0
    for n, d in instructions:
        new_r, new_c = add_tuples((r, c), scalar_multiply(int(n), DIRECTION_VECTORS[d]))
        endpoints.add(min(r, new_r))
        endpoints.add(max(r, new_r) + 1)
        r, c = new_r, new_c
    sorted_endpoints = sorted(list(endpoints))
    return [(sorted_endpoints[i], sorted_endpoints[i + 1]) for i in range(len(sorted_endpoints) - 1)]

# We only need to record the border for one row in each interval
def get_grid_border(instructions, row_intervals):
    grid_border = dict()
    r, c = 0, 0
    for i in range(len(instructions)):
        n, d = instructions[i]
        next_i, prev_i = (i + 1) % len(instructions), (i - 1) % len(instructions)
        next_d, prev_d = instructions[next_i][1], instructions[prev_i][1]
        new_r, new_c = add_tuples((r, c), scalar_multiply(n, DIRECTION_VECTORS[d]))
        if d in "LR":
            interval = (min(c, new_c), max(c, new_c) + 1, next_d == prev_d)
            grid_border[r] = grid_border.get(r, []) + [interval]
        else:
            for interval in row_intervals:
                i_r = interval[0]
                if min(r, new_r) < i_r < max(r, new_r):
                    grid_border[i_r] = grid_border.get(i_r, []) + [(c, c + 1, True)]
        r, c = new_r, new_c
    return grid_border

def count_internal_area(grid_border, row_intervals):
    count = 0
    for row_interval in row_intervals:
        this_row_count = 0
        col_intervals = sorted(grid_border[row_interval[0]], key=lambda x: x[0])
        crosses = 0
        prev_c = col_intervals[0][1]
        for col_interval in col_intervals:
            this_row_count += col_interval[1] - col_interval[0]
            if crosses % 2 == 1:
                this_row_count += col_interval[0] - prev_c
            if col_interval[2]:
                crosses += 1
            prev_c = col_interval[1]
        count += this_row_count * (row_interval[1] - row_interval[0])
    return count

def solve_part(input_list, extract_instruction):
    instructions = [extract_instruction(line) for line in input_list]
    row_intervals = get_row_intervals(instructions)
    row_intervals = get_row_intervals(instructions)
    grid_border = get_grid_border(instructions, row_intervals)
    return count_internal_area(grid_border, row_intervals)

# input_list: list[str]
def solve(input_list):
    def extract_instruction_p1(line):
        return (int(line.split()[1]), line.split()[0])
    def extract_instruction_p2(line):
        return (int(line[-7:-2], 16), "RDLU"[int(line[-2])])
    return (solve_part(input_list, extract_instruction_p1),
            solve_part(input_list, extract_instruction_p2))

# Runs in less than 0.1 seconds on my machine
sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")