from util import *

def is_equation_true(target, nums, is_p1):
    if len(nums) == 1:
        return target == nums[0]
    if nums[0] > target:
        return False
    truth = (
        is_equation_true(target, [nums[0] + nums[1]] + nums[2:], is_p1)
        or is_equation_true(target, [nums[0] * nums[1]] + nums[2:], is_p1)
    )
    return truth if is_p1 else (
        truth or is_equation_true(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:], is_p1)
    )

# input_list: list[str]
def solve(input_list):
    p1, p2 = 0, 0
    for target, nums in input_list:
        target, nums = int(target), [int(n) for n in nums.split(" ")]
        p1 += target if is_equation_true(target, nums, is_p1=True) else 0
        p2 += target if is_equation_true(target, nums, is_p1=False) else 0
    return p1, p2

# Runs in under 2 seconds on my machine
sample_input = get_list_of_strings("sample_input_puzzle_7.txt", separation=": ")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_7.txt", separation=": ")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")