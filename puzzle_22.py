from util import *
from collections import deque

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_22.txt")
input = get_list_of_strings("input_puzzle_22.txt")

def process_bricks(raw_bricks):
    bricks = []
    for raw_brick in raw_bricks:
        x1, y1, z1, x2, y2, z2 = map(lambda x: int(x), raw_brick.replace("~", ",").split(","))
        xy_coords = set()
        current = (x1, y1)
        dist = abs(y2 - y1 + x2 - x1)
        dir_vect = ((x2 - x1) // max(dist, 1), (y2 - y1) // max(dist, 1))
        for i in range(dist + 1):
            xy_coords.add(current)
            current = add_tuples(current, dir_vect)
        bricks.append((xy_coords, (z1, z2 + 1)))
    return bricks

def drop_bricks(bricks):
    # All x, y coordinates are in [0, 10) x [0, 10)
    lowest_points = [[(1, None) for i in range(10)] for j in range(10)]
    bricks_above, bricks_below = dict(), dict()
    for i, brick in enumerate(bricks):
        drop_height = max([lowest_points[x][y][0] for (x, y) in brick[0]])
        bricks_above[i], bricks_below[i] = set(), set()
        for (x, y) in brick[0]:
            brick_below = lowest_points[x][y][1]
            if brick_below is not None and lowest_points[x][y][0] == drop_height:
                bricks_below[i].add(brick_below)
                bricks_above[brick_below].add(i)
            lowest_points[x][y] = (brick[1][1] - brick[1][0] + drop_height, i)
    return bricks_above, bricks_below

# input_list: list[str]
def solve(input_list):
    bricks = sorted(process_bricks(input_list), key=lambda T: T[1][0])
    bricks_above, bricks_below = drop_bricks(bricks)
    safe_brick_count, fallen_bricks_count = 0, 0
    for brick in sorted(bricks_above):
        queue = deque([brick])
        fallen_bricks = {brick}
        while not len(queue) == 0:
            current_brick = queue.popleft()
            for brick_above in bricks_above[current_brick]:
                if bricks_below[brick_above].issubset(fallen_bricks):
                    queue.append(brick_above)
                    fallen_bricks.add(brick_above)
        fallen_bricks_count += len(fallen_bricks) - 1
        # Python converts True to 1 and False to 0
        safe_brick_count += len(fallen_bricks) == 1
    return safe_brick_count, fallen_bricks_count

# Runs in just about 2 seconds on my machine
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")