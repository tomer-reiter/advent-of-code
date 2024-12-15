from util import *
# This solution hasn't been cleaned up very much, I may come back later to clean it up

def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                grid[r][c] = "."
                return r, c

# input_list: list[str]
def solve(input_list):
    grid, instructions = input_list[0], "".join(input_list[1])
    grid = [[c for c in line] for line in grid]
    robot = find_start(grid)
    for d in instructions:
        r, c = add_tuples(robot, DIRECTION_VECTORS[d])
        if grid[r][c] == ".":
            robot = r, c
        elif grid[r][c] == "O":
            while grid[r][c] == "O":
                r, c = add_tuples((r, c), DIRECTION_VECTORS[d])
            if grid[r][c] == ".":
                grid[r][c] = "O"
                robot = add_tuples(robot, DIRECTION_VECTORS[d])
                grid[robot[0]][robot[1]] = "."
    p1 = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                p1 += 100 * r + c
    doubled_width = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    grid = ["".join([doubled_width[c] for c in line]) for line in input_list[0]]
    grid = [[c for c in line] for line in grid]
    robot = find_start(grid)
    count = 0
    for d in instructions:
        count += 1
        r, c = add_tuples(robot, DIRECTION_VECTORS[d])
        if grid[r][c] == ".":
            robot = r, c
        elif grid[r][c] in "[]":
            seen_symbols = []
            if grid[r][c] == "#":
                continue
            if d in "<>":
                while grid[r][c] in "[]":
                    seen_symbols += [grid[r][c]]
                    r, c = add_tuples((r, c), DIRECTION_VECTORS[d])
                if grid[r][c] == ".":
                    robot = add_tuples(robot, DIRECTION_VECTORS[d])
                    r, c = robot
                    grid[r][c] = "."
                    for symbol in seen_symbols:
                        r, c = add_tuples((r, c), DIRECTION_VECTORS[d])
                        grid[r][c] = symbol
            else:
                other_col = c + 1 if grid[r][c] == "[" else c - 1
                start_box = ((r, c), (r, other_col))
                boxes_this_row = [start_box]
                boxes = [boxes_this_row]
                move_valid = True
                while len(boxes_this_row) > 0:
                    boxes_this_row = []
                    for box in boxes[-1]:
                        for box_r, box_c in box:
                            new_box_r, new_box_c = add_tuples((box_r, box_c), DIRECTION_VECTORS[d])
                            if grid[new_box_r][new_box_c] in "[]":
                                other_col = new_box_c + 1 if grid[new_box_r][new_box_c] == "[" else new_box_c - 1
                                if (((new_box_r, new_box_c), (new_box_r, other_col)) not in boxes_this_row
                                    and ((new_box_r, other_col), (new_box_r, new_box_c)) not in boxes_this_row):
                                    boxes_this_row += [((new_box_r, new_box_c), (new_box_r, other_col))]
                            if grid[new_box_r][new_box_c] == "#":
                                move_valid = False
                    boxes += [boxes_this_row]
                if move_valid:
                    for boxes_row in reversed(boxes):
                        for box in boxes_row:
                            for r, c in box:
                                new_r, new_c = add_tuples((r, c), DIRECTION_VECTORS[d])
                                grid[new_r][new_c] = grid[r][c]
                                grid[r][c] = "."
                    robot = add_tuples(robot, DIRECTION_VECTORS[d])
    p2 = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "[":
                p2 += 100 * r + c
    return p1, p2

sample_input = get_list_of_strings("sample_input_puzzle_15.txt", line_break="\n\n")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_15.txt", line_break="\n\n")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")