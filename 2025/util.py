# Returns a list of strings, one per line. Empty lines will be 
# an empty string in the list
def get_list_of_strings(input_file_path, line_break=None, separation=None):
    with open(input_file_path) as input_file:
        input_parsed = input_file.read()
    if line_break is not None and separation is not None:
        input_line_broken = [group.splitlines() for group in input_parsed.split(line_break)]
        return [[line.split(separation) for line in group_of_lines] for group_of_lines in input_line_broken]
    elif line_break is not None:
        return [group.splitlines() for group in input_parsed.split(line_break)]
    elif separation is not None:
        return [line.split(separation) for line in input_parsed.splitlines()]
    else:
        return input_parsed.splitlines()

# Must have tuples of the same length
def add_tuples(tuple_1, tuple_2):
    if len(tuple_1) != len(tuple_2):
        return None
    else:
        return tuple(map(lambda i, j: i + j, tuple_1, tuple_2))

# Must have tuples of same length
def combine_tuples(tuple_1, tuple_2, op):
    if len(tuple_1) != len(tuple_2):
        return None
    else:
        return tuple(map(op, tuple_1, tuple_2))
    
def scalar_multiply(n, t):
    return tuple(map(lambda x: n * x, t))

def transform_tuple(op, t):
    return tuple(map(op, t))

# Requires that grid is a 2d array type with equal length rows
def is_in_bounds(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

DIRECTION_VECTORS = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}