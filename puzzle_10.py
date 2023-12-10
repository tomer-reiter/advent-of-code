from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_10.txt")
input = get_list_of_strings("input_puzzle_10.txt")

u = (-1, 0)
d = (1, 0)
r = (0, 1)
l = (0, -1)

pipe_dirs = {
    "L": (u, r),
    "-": (l, r),
    "|": (u, d),
    "F": (d, r),
    "J": (l, u),
    "7": (l, d),
}

# Finds the start as well as the two pipes pointing two it. There are always
# exactly two pointing to the start in all examples and inputs, which helps
# simplify a few things throughout. E.g. we always stay on the loop while
# traversing
def find_the_start(input_list):
    for i in range(len(input_list)):
        if "S" in input_list[i]:
            start_coords = (i, input_list[i].index("S"))
    connecting_pipes = dict()
    dirs_from_start = ()
    # Find the pipes pointing to the start
    for dir in [u, l, d, r]:
        x,y = add_tuples(start_coords, dir)
        if not (0 <= x < len(input_list) and 0 <= y < len(input_list[0])):
            continue
        pipe = input_list[x][y]
        if pipe != ".":
            out_dirs = pipe_dirs[pipe]
            opp_dir = tuple(-coord for coord in dir)
            if opp_dir in out_dirs:
                other_dir = out_dirs[1 - out_dirs.index(opp_dir)]
                connecting_pipes[(x,y)] = other_dir, [start_coords, (x,y)]
                dirs_from_start += (dir,)
    # Replace the start with the pipe shape it should be. This will help in p2
    for pipe, (d1, d2) in pipe_dirs.items():
        if (d1, d2) == dirs_from_start or (d2, d1) == dirs_from_start:
            s_x, s_y = start_coords
            line = input_list[s_x]
            input_list[s_x] = line[:s_y] + pipe + line[s_y+1:]
    return connecting_pipes

def find_loop(input_list):
    border = find_the_start(input_list)
    loop_found = False
    distance = 1
    while not loop_found:
        distance += 1
        new_border = dict()
        for (x,y), (dir, path) in border.items():
            x_new, y_new = add_tuples((x,y), dir)
            if (x_new, y_new) in new_border:
                loop_found = True
                loop = path[1:] + new_border[(x_new, y_new)][1]
                return loop, distance
            new_pipe_dirs = pipe_dirs[input_list[x_new][y_new]]
            # backward_dir and forward_dir are backwards and forwards along
            # the loop at the point of the new pipe
            backward_dir = tuple(-coord for coord in dir)
            forward_dir = new_pipe_dirs[1 - new_pipe_dirs.index(backward_dir)]
            new_border[(x_new,y_new)] = forward_dir, path + [(x_new, y_new)]
        border = new_border

# input_list: list[str]
def solve(input_list):
    loop, distance = find_loop(input_list)
    loop = set(loop)
    enclosed_tiles = 0 
    for i in range(len(input_list)):
        this_row = ""
        for j in range(len(input_list[i])):
            this_row += input_list[i][j] if (i,j) in loop else "."
        # For these substrings, we're not crossing into or out of the enclosed
        # area. E.g. in ..L---J.. were either inside or outside the entire time
        for substring in ["-", "LJ", "F7"]:
            this_row = this_row.replace(substring, "")
        # For | and these substrings, we do cross a boundary
        for substring in ["L7", "FJ"]:
            this_row = this_row.replace(substring, "|")
        pipes_crossed = 0
        for c in this_row:
            if c == "." and pipes_crossed % 2 == 1:
                enclosed_tiles += 1
            elif c == "|":
                pipes_crossed += 1
    return distance, enclosed_tiles

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")