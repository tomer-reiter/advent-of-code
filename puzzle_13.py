from util import *
import copy

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_13.txt")
input = get_list_of_strings("input_puzzle_13.txt")

def get_grids(input_list):
    grids = []
    grid = []
    for line in input_list + [""]:
        if line == "":
            grids.append(grid)
            grid = []
        else:
            grid.append(line)
    return grids

def transpose(grid):
    return ["".join(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]

def has_horizontal_sym(grid):
    rows = dict()
    syms = []
    for row in grid:
        rows[row] = rows.get(row, chr(len(rows) + 1))
    rows_string = "".join(rows[row] for row in grid)
    prefix_reversed, suffix = "", rows_string
    for i in range(len(rows_string) - 1):
        prefix_reversed = suffix[0] + prefix_reversed
        suffix = suffix[1:]
        common_length = min(len(prefix_reversed), len(suffix))
        if prefix_reversed[:common_length] == suffix[:common_length]:
            syms.append(i + 1)
    return syms

def line_of_symmetry_includes_smudge(lines, smudged_line, num_rows):
    if lines <= num_rows // 2:
        return smudged_line in range(lines*2)
    else:
        return smudged_line in range(lines*2 - num_rows, num_rows)

def find_horizontal_smudge(grid):
    for i in range(len(grid)):
        for j in range(i):
            row_i, row_j = grid[i], grid[j]
            if len([k for k in range(len(row_i)) if row_i[k] != row_j[k]]) == 1:
                new_grid = copy.copy(grid)
                new_grid[i] = row_j
                syms = has_horizontal_sym(new_grid)
                for sym_line in syms:
                    if line_of_symmetry_includes_smudge(sym_line, i, len(grid)):
                        return True, sym_line
                new_grid[i], new_grid[j] = row_i, row_i
                syms = has_horizontal_sym(new_grid)
                for sym_line in syms:
                    if line_of_symmetry_includes_smudge(sym_line, j, len(grid)):
                        return True, sym_line
    return False, 0


# input_list: list[str]
def solve(input_list):
    grids = get_grids(input_list)
    p1, p2 = 0, 0
    for grid in grids:
        syms = has_horizontal_sym(grid)
        score = syms[0] * 100 if len(syms) > 0 else has_horizontal_sym(transpose(grid))[0]
        p1 += score
        found, sym_line = find_horizontal_smudge(grid)
        score = sym_line * 100 if found else find_horizontal_smudge(transpose(grid))[1]
        p2 += score
    return p1, p2


sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")