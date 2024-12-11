from util import *
from functools import cache

def transform_single(s):
    if s == "0":
        return ("1",)
    elif len(s) % 2 == 0:
        first_half, second_half = s[:len(s) // 2], s[len(s) // 2:]
        return (str(int(first_half)), str(int(second_half)))
    else:
        return (str(2024 * int(s)),)

@cache
def transform_n_times(s, n):
    if n == 0:
        return 1
    return sum([transform_n_times(s_new, n - 1) for s_new in transform_single(s)])

# input_list: list[str]
def solve(input_list):
    return (
        sum([transform_n_times(s, 25) for s in input_list[0]]),
        sum([transform_n_times(s, 75) for s in input_list[0]]),
    )

sample_input = get_list_of_strings("sample_input_puzzle_11.txt", separation=" ")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_11.txt", separation=" ")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")