from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_11.txt")
input = get_list_of_strings("input_puzzle_11.txt")

# input_list: list[str]
def solve(input_list, enlarge_factor):
    total_distance = 0
    adj_row_counts = dict()
    col_counts = dict()
    offset = 0
    for i in range(len(input_list)):
        row = input_list[i]
        galaxy_cols = [j for j in range(len(row)) if row[j] == "#"]
        this_row_count = len(galaxy_cols)
        if this_row_count == 0:
            offset += enlarge_factor
            continue
        for col in galaxy_cols:
            col_counts[col] = col_counts.get(col, 0) + 1
        for adj_row, count in adj_row_counts.items():
            # Manhattan distance is x_dist + y_dist, so we can just add all the
            # x_dist values first
            total_distance += (i + offset - adj_row) * this_row_count * count
        adj_row_counts[i + offset] = this_row_count
    adj_col_counts = dict()
    offset = 0
    for j in range(len(input_list[0])):
        if not j in col_counts:
            offset += enlarge_factor
            continue
        for adj_col, count in adj_col_counts.items():
            total_distance += (j + offset - adj_col) * col_counts[j] * count
        adj_col_counts[j + offset] = col_counts[j]
    return total_distance


sample_p1 = solve(sample_input, 1)
p1 = solve(input, 1)
sample_p2 = solve(sample_input, 99)
p2 = solve(input, 999999)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")