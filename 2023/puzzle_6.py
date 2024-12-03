from util import *
from functools import reduce
import math

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_6.txt")
input = get_list_of_strings("input_puzzle_6.txt")

# input_list: list[str]
def solve(input_list):
    p1 = 1
    values = list(map(lambda x: x.split(": ")[1], input_list))
    times, distances = list(map(lambda x: x.split(), values))
    p2time = int(reduce(lambda x,y: x + y, times))
    p2distance = int(reduce(lambda x,y: x + y, distances))
    times = list(map(lambda x: int(x), times))
    distances = list(map(lambda x: int(x), distances))
    for time, distance in list(zip(times, distances)):
        p1_count = 0
        for x in range(time):
            if x * (time - x) > distance:
                p1_count += 1
        p1 *= p1_count
    # Quadratic formula to find the zeroes
    p2_upper_zero = math.floor(0.5*(-p2time + (p2time ** 2 - 4 * p2distance) ** 0.5))
    p2_lower_zero = math.ceil(0.5*(-p2time - (p2time ** 2 - 4 * p2distance) ** 0.5))
    return p1, p2_upper_zero - p2_lower_zero + 1

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")