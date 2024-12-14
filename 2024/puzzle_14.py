from util import *
from math import prod

def parse(s):
    return [int(n) for n in s[2:].split(",")]

def move_n(guards, x_max, y_max, n):
    return [
        ((px + n * vx) % x_max, (py + n * vy) % y_max) for px, py, vx, vy in guards
    ]

def quadrant_count(guards, x_max, y_max):
    q_count = {i: 0 for i in range(4)}
    for x, y in guards:
        if x == x_max // 2 or y == y_max // 2:
            continue
        q_count[2*(x < x_max // 2) + (y < y_max // 2)] += 1
    return q_count

def print_guards(guards, x_max, y_max):
    for y in range(y_max):
        s = ""
        for x in range(x_max):
            s += "#" if (x, y) in guards else "."
        print(s)

# The idea here is that if you have an image of a christmas tree, it will have a big clump near
# the middle vertical line, and near the base of the tree horizontally. Of course, if you've done
# this problem you know the christmas tree looks nothing like the christmas tree emoji. This does
# still work though!
def part_two(guards, x_max, y_max):
    mods, best = [0, 0], [0, 0]
    for i in range(2):
        for n in range([x_max, y_max][i]):
            new_guards = move_n(guards, x_max, y_max, n)
            count_max = max(
                [list(map(lambda p: p[i], new_guards)).count(j) for j in range([x_max, y_max][i])]
            )
            if count_max > best[i]:
                mods[i] = n
                best[i] = count_max
    # You really want the Chinese Remainder Theorem here. But this isn't a very big range
    # to search in
    for n in range(x_max * y_max):
        if n % x_max == mods[0] and n % y_max == mods[1]:
            return n

# input_list: list[str]
def solve(input_list, is_sample):
    x_max = 11 if is_sample else 101
    y_max = 7 if is_sample else 103
    guards = [parse(line[0]) + parse(line[1]) for line in input_list]
    p1_guards = move_n(guards, x_max, y_max, 100)
    if not is_sample:
        p2 = part_two(guards, x_max, y_max)
        print_guards(move_n(guards, x_max, y_max, p2), x_max, y_max)
    return prod(quadrant_count(p1_guards, x_max, y_max).values()), None if is_sample else p2

sample_input = get_list_of_strings("sample_input_puzzle_14.txt", separation=" ")
sample_p1, sample_p2 = solve(sample_input, True)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_14.txt", separation=" ")
p1, p2 = solve(input, False)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")