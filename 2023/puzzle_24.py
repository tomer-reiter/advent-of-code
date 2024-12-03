from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_24.txt")
input = get_list_of_strings("input_puzzle_24.txt")

def get_hailstone_info(hailstones):
    hailstone_info = []
    for hailstone in hailstones:
        values = tuple(map(lambda x: int(x), hailstone.replace("@", ",").split(", ")))
        hailstone_info.append((values[:3], values[3:]))
    return hailstone_info

def test_x_y_intersect(hailstone1, hailstone2, c_min, c_max):
    x1, y1, vx1, vy1 = hailstone1[0][:2] + hailstone1[1][:2]
    x2, y2, vx2, vy2 = hailstone2[0][:2] + hailstone2[1][:2]
    det = vx1 * vy2 - vx2 * vy1
    if det == 0:
        return False
    a = (vy2 * (x2 - x1) + vx2 * (y1 - y2)) / det
    b = (vy1 * (x2 - x1) + vx1 * (y1 - y2)) / det
    if a <= 0 or b <= 0:
        return False
    x, y = x1 + a * vx1, y1 + a * vy1
    return c_min <= x <= c_max and c_min <= y <= c_max

# input_list: list[str]
def solve(input_list, c_min, c_max):
    hailstones = get_hailstone_info(input_list)
    test_area_count = 0 
    for i in range(len(hailstones)):
        for j in range(i):
            hailstone1, hailstone2 = hailstones[i], hailstones[j]
            if test_x_y_intersect(hailstone1, hailstone2, c_min, c_max):
                test_area_count += 1
    return test_area_count

# When solving part 2, I mistakenly thought that each hailstone gives you 3
# linear equations with 7 variables: time to collision for that hailstone and
# the 6 starting coordinate and velocity variables for the rock. So if you use
# info from 3 hailstones you get 9 variables and 9 equations. I was in a
# hurry so I put it into Sage math to solve (you can execute code here:
# https://sagecell.sagemath.org/). Here's the code which produced the correct
# answer for part 2. The last line prints the answer. Each hailstone is a tuple
# of the 6 values in the order they appear in the input.
# rx, ry, rz, vx, vy, vz, t1, t2, t3 = var("rx, ry, rz, vx, vy, vz, t1, t2, t3")
# eqns = []
# hailstones = [hailstone1, hailstone2, hailstone3]
# for i in range(1):
#     t_var = [t1, t2, t3][i]
#     hailstone = hailstones[i]
#     for j in range(3):
#         r, v, point_coord, point_velo = [rx, ry, rz][j], [vx, vy, vz][j], hailstone[j], hailstone[3 + j]
#         eqns.append(r == point_coord + t_var * (point_velo - v))
# solutions = solve(eqns, rx, ry, rz, vx, vy, vz, t1, t2, t3)
# (rx + ry + rz).subs(solutions[0]) 
# It turns out these equations aren't linear, so you couldn't solve this from
# first principles using only linear algebra. I may update this to avoid using
# Sage, but it likely won't be today

sample_p1 = solve(sample_input, 7, 27)
print(f"Part 1 answer for sample input: {sample_p1}")
# print(f"Part 2 answer for sample input: {sample_p2}")
p1 = solve(input, 200000000000000, 400000000000000)
print(f"Part 1 final answer: {p1}")
# print(f"Part 2 final answer: {p2}")