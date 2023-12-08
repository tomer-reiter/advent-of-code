from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_3.txt")
input = get_list_of_strings("input_puzzle_3.txt")

def get_symbol_map(input_list):
    symbol_map = dict()
    symbols = set()
    for i in range(len(input_list)):
        line = input_list[i]
        for j in range(len(line)):
            char = line[j]
            if char != "." and not char.isnumeric():
                symbol_map[(i, j)] = []
                symbols.add(char)
    return symbol_map

# input_list: list[str]
def solve(input_list):
    p1 = 0
    p2 = 0
    symbol_map = get_symbol_map(input_list)
    for i in range(len(input_list)):
        line = input_list[i]
        start = -2
        end = -2
        number = ""
        for j in range(len(line)):
            char = line[j]
            if char.isnumeric():
                if number != "":
                    end = j
                    number += char
                else:
                    start = j
                    end = j
                    number += char
            if (not char.isnumeric() or j == len(line) - 1) and number != "":
                symbol_found = False
                for i1 in range(i-1, i+2):
                    for j1 in range(start-1, end+2):
                        if (i1, j1) in symbol_map:
                            symbol_found = True
                            symbol_map[(i1, j1)] = symbol_map[(i1,j1)] + [int(number)]
                if symbol_found:
                    p1 += int(number)
                number = ""
    for symbol, nums in symbol_map.items():
        if input_list[symbol[0]][symbol[1]] == "*" and len(nums) == 2:
            p2 += nums[0] * nums[1]
    return p1, p2

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")