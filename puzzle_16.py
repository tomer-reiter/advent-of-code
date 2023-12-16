from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_16.txt")
input = get_list_of_strings("input_puzzle_16.txt")

direction_vector = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

# Shows the next heading(s) if you're at that symbol, in the order of NESW
next_heading = {
    ".": ["N", "E", "S", "W"],
    "/": ["E", "N", "W", "S"],
    "\\": ["W", "S", "E", "N"],
    "-": ["EW", "E", "EW", "W"],
    "|": ["N", "NS", "S", "NS"],
}

def is_in_bounding_box(coords, grid):
    return 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])

def get_next_coords(coords, grid):
    coords, heading = coords[:2], coords[2]
    new_headings = next_heading[grid[coords[0]][coords[1]]]["NESW".find(heading)]
    new_coords = []
    for new_heading in new_headings:
        new_coord = add_tuples(coords, direction_vector[new_heading]) + (new_heading,)
        new_coords.append(new_coord)
    return new_coords

def get_energized_count(grid, start_heading):
    # For visited squares we keep track of both the coordinates and the heading, because
    # the same square with a different heading could result in a different path
    border, visited = set([start_heading]), set([start_heading])
    while len(border) > 0:
        new_border = set()
        for coords in border:
            for new_coords in get_next_coords(coords, grid):
                if is_in_bounding_box(new_coords[:2], grid) and not new_coords in visited:
                    new_border.add(new_coords)
                    visited.add(new_coords)
        border = new_border
    return len(set(map(lambda x: x[:2], visited)))


# input_list: list[str]
def solve(input_list):
    p1 = get_energized_count(input_list, (0, 0, "E"))
    p2 = 0
    n = len(input_list) # The inputs are squares
    for i in range(n):
        for start in [(0, i, "S"), (n - 1, i, "N"), (i, n - 1, "W"), (i, 0, "E")]:
            count = get_energized_count(input_list, start)
            p2 = max(p2, count)
    return p1, p2

# Runs in under 7 seconds on my machine
sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")