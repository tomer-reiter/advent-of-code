from util import *
from functools import reduce

def shortest_path(n, fallen_bytes):
    visited, boundary = {(0, 0)}, {(0, 0)}
    dist = 0
    while True:
        dist += 1
        new_boundary = set()
        for p in boundary:
            for d in "^>v<":
                new_p = add_tuples(p, DIRECTION_VECTORS[d])
                if new_p == (n - 1, n - 1):
                    return dist
                if (new_p not in fallen_bytes and new_p not in visited
                    and 0 <= new_p[0] < n and 0 <= new_p[1] < n):
                    new_boundary.add(new_p)
                    visited.add(new_p)
        if len(new_boundary) == 0:
            return -1
        boundary = new_boundary

def is_blocked(n, S):
    row_vals, col_vals = map(lambda x: x[0], S), map(lambda x: x[1], S)
    top, bottom = 0 in row_vals, n - 1 in row_vals
    left, right = 0 in col_vals, n - 1 in col_vals
    return (bottom and (top or right)) or (left and (top or right))

# This is an overoptimization, using shortest_path and just trying to add one byte at a time
# ran in ~50s. But this runs in ~0.5s by instead keeping track of the groups of bytes
def first_blockage(n, all_bytes):
    components = []
    for byte in all_bytes:
        neighbors = []
        for d in [(a, b) for a in range(-1, 2) for b in range(-1, 2)]:
            neighbor = add_tuples(byte, d)
            neighbors += [i for i in range(len(components)) if neighbor in components[i]]
        new_comp = reduce(lambda x, y: x.union(y), [components[i] for i in neighbors], set())
        new_comp.add(byte)
        if is_blocked(n, new_comp):
            return byte
        for i in sorted(list(set(neighbors)), reverse=True):
            del components[i]
        components += [new_comp]

# input_list: list[str]
def solve(input_list, is_sample):
    n = 7 if is_sample else 71
    bytes = [eval(t) for t in input_list]
    bytes_fallen = 12 if is_sample else 1024
    return shortest_path(n, set(bytes[:bytes_fallen])), first_blockage(n, bytes)

sample_input = get_list_of_strings("sample_input_puzzle_18.txt")
sample_p1, sample_p2 = solve(sample_input, is_sample=True)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_18.txt")
p1, p2 = solve(input, is_sample=False)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")