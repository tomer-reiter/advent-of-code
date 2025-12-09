from util import *

# Note that the algorithm throughout assumes no two x-coords in the input are off by 1 (and assumes
# the same of the y-coords). This is true for my input, and could also be accomplished by
# multiplying everything by 2

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def xs_contained(x1, x2, bounds):
    return any([bounds[i] <= x1 and x2 <= bounds[i + 1] for i in range(0, len(bounds), 2)])

def is_in_interior(p1, p2, interior):
    x1, x2, y1, y2 = min(p1[0], p2[0]), max(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[1], p2[1])
    for y_low, y_high in interior:
        if (y1 <= y_high and y_low <= y2) and not xs_contained(x1, x2, interior[(y_low, y_high)]):
            return False
    return True

# input_list: list[str]
def solve(input_list):
    pts = [(int(p[0]), int(p[1])) for p in input_list]
    # maps a range of x to a union of ranges for y that are in the interior of the shape
    interior = dict()
    # maps an x coordinate to the list of y coords that there's a corner in our shape
    h_lines = dict()
    for i in range(len(pts)):
        j = (i + 1) % len(pts)
        p1, p2 = pts[i], pts[j]
        if p1[1] == p2[1]:
            h_lines[p1[1]] = h_lines.get(p1[1], []) + [p1[0], p2[0]]
    y_values, x_values = sorted(h_lines.keys()), []
    for i in range(len(y_values) - 1):
        x_values = sorted(x_values + h_lines[y_values[i]])
        for x in set(x_values):
            if x_values.count(x) == 2:
                x_values.remove(x), x_values.remove(x)
        interior[(y_values[i] + 1, y_values[i + 1] - 1)] = x_values
    pt_pairs = [(pts[i], pts[j]) for i in range(len(pts)) for j in range(i + 1, len(pts))]
    return (
        max([area(*pts) for pts in pt_pairs]),
        max([area(*pts) for pts in pt_pairs if is_in_interior(*pts, interior)])
    )

sample_input = get_list_of_strings("sample_input_puzzle_9.txt", separation=",")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_9.txt", separation=",")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")