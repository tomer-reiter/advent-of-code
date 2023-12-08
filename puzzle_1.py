from util import *

# Comment this out if skipping testing on sample input
sample_input_p1 = get_list_of_strings("sample_input_puzzle_1_p1.txt")
sample_input_p2 = get_list_of_strings("sample_input_puzzle_1_p2.txt")
input = get_list_of_strings("input_puzzle_1.txt")

# Note that here and in the next function, input_list: list[str]!
def part_one(input_list):
    total_calibration = 0
    for line in input_list:
        numerals = list(filter(lambda c: c.isnumeric(), line))
        calibration = int(numerals[0] + numerals[-1])
        total_calibration += calibration
    return total_calibration

def part_two(input_list):
    adjusted_list = []
    spelled_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in input_list:
        new_line = line
        for i in range(9):
            new_line = new_line.replace(spelled_nums[i], spelled_nums[i] + str(i+1) + spelled_nums[i])
        adjusted_list.append(new_line)
    return part_one(adjusted_list)


# Part 1
print(f"Part 1 answer for sample input: {part_one(sample_input_p1)}")
print(f"Part 1 final answer: {part_one(input)}")

# Part 2 
print(f"Part 2 answer for sample input: {part_two(sample_input_p2)}")
print(f"Part 2 final answer: {part_two(input)}")