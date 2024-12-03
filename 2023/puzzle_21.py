from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_21.txt")
input = get_list_of_strings("input_puzzle_21.txt")

def find_the_start(grid):
    for i in range(len(grid)):
        if "S" in grid[i]:
            return (i, grid[i].index("S"))
        
def take_one_step(grid, visited, border, is_p1=True):
    new_border = set()
    for p in border:
        for d in "NESW":
            if is_p1:
                new_p = add_tuples(p, DIRECTION_VECTORS[d])
                is_new_and_valid_coord = (not new_p in visited) and is_in_bounds(new_p[0], new_p[1], grid)
            else:
                q = add_tuples(p[:2], DIRECTION_VECTORS[d])
                new_p = q[0] % len(grid), q[1] % len(grid[0])
                new_p = new_p + add_tuples((q[0] // len(grid), q[1] // len(grid[0])), p[2:])
                is_new_and_valid_coord = not new_p in visited
            if is_new_and_valid_coord and (grid[new_p[0]][new_p[1]] != "#"):
                new_border.add(new_p)
                visited.add(new_p)
    return new_border

def is_quadratic(L, len_grid):
    if not len(L) >= 4:
        return False, None
    y_values = list(map(lambda x: x[1], L[-4:]))
    c = y_values[1]
    b = (y_values[2] - y_values[0]) // 2
    a = y_values[0] + b - c
    if not a * 2 ** 2 + b *2 + c == y_values[3]:
        return False, None
    def q(n):
        m = ((n // 2) - L[-3][0]) // len_grid
        return a * m **2 + b * m + c
    return True, q

# The key observation here, which I made by looking at some data, is that after
# some point, this function is when considering every 2 * len(grid) values.
# That is, there exists an M such that if m >= M, then the function
# g_m(x) := find_tiles(m + 2x*len(grid)) is quadratic for x >= 0. I don't have
# a proof for this, but here is a heuristic explanation. Once you get to a
# corner point on any copy of the original grid, to get to the same corner on
# the next grid in that direction takes 2len(grid) steps. So you see repeating
# patterns in cycles of that length. The function should be asymptotically
# quadratic: e.g. an empty grid would give 4, 4 + 8, 4 + 8 + 12, ...
def find_tiles_at_dist_n(grid, start, n, is_p1 = True):
    visited, border = set([start]), set([start])
    reachable = set()
    target_mod_values = []
    for i in range(n):
        if i % 2 == n % 2:
            reachable = reachable.union(border)
            if (i // 2) % len(grid) == (n // 2) % len(grid):
                target_mod_values.append((i // 2, len(reachable)))
                quadratic, quadratic_fn = is_quadratic(target_mod_values, len(grid))
                if quadratic:
                    return quadratic_fn(n)
        border = take_one_step(grid, visited, border, is_p1=is_p1)
    return len(reachable.union(border))

# input_list: list[str]
def solve(input_list, n, is_p1=True):
    start = find_the_start(input_list)
    # For part 2, we'll record (x, y, a, b), where (x, y) is coords on the
    # original grid, and (a, b) is coords for which grid we're on
    start = start if is_p1 else (start[0], start[1], 0, 0)
    return find_tiles_at_dist_n(input_list, start, n, is_p1=is_p1)

# Runs in just under 25 seconds on my machine
sample_p1 = solve(sample_input, 6)
p1 = solve(input, 64)
sample_p2 = solve(sample_input, 5000, False)
p2 = solve(input, 26501365, False)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")