from util import *

# When flood_fill_only=True: just return the set of points in the region
# Otherwise, compute the prices of the region for p1 and p2 and return those
def points_price(grid, start, points, flood_fill_only):
    area= 1
    sides = {d: set() for d in "NESW"}
    boundary, all_visited = {start}, {start}
    while len(boundary) > 0:
        new_boundary = set()
        for r, c in boundary:
            for d in "NESW":
                p1 = add_tuples(DIRECTION_VECTORS[d], (r, c))
                r1, c1 = p1
                if flood_fill_only:
                    if p1 in points and not p1 in all_visited:
                        all_visited.add(p1), new_boundary.add(p1)
                elif not is_in_bounds(r1, c1, grid) or grid[r1][c1] != grid[r][c]:
                    sides[d].add(p1)
                elif p1 not in all_visited:
                    area += 1
                    all_visited.add(p1), new_boundary.add(p1)
        boundary = new_boundary
    if flood_fill_only:
        return all_visited
    return (
        area * sum([len(sides[d]) for d in "NESW"]),
        area * sum([flood_fill(grid, sides[d], True) for d in "NESW"]), 
        all_visited,
    )


# When flood_fill_only=True: return the number of regions
# Otherwise, compute the prices of all regions for p1 and p2 and return those
def flood_fill(grid, points, flood_fill_only):
    processed = set()
    p1, p2, components = 0, 0, 0
    for p in points:
        if p in processed:
            continue
        components += 1
        result = points_price(grid, p, points, flood_fill_only)
        region = result if flood_fill_only else result[2]
        processed = processed.union(region)
        if not flood_fill_only:
            p1, p2 = p1 + result[0], p2 + result[1]
    return components if flood_fill_only else (p1, p2)

# input_list: list[str]
def solve(input_list):
    return flood_fill(
        input_list,
        [(r, c) for r in range(len(input_list)) for c in range(len(input_list[0]))],
        False
    )

sample_input = get_list_of_strings("sample_input_puzzle_12.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_12.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")