from util import *
from functools import reduce

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_5.txt")
input = get_list_of_strings("input_puzzle_5.txt")

def get_number_map(mapping):
    def map_number(x):
        for source_range, offset in mapping.items():
            if source_range[0] <= x < source_range[1]:
                return x + offset
        return x
    return map_number

def get_range_map(mapping):
    def map_range(x, n):
        new_ranges = []
        current = x
        while current < x + n - 1:
            found_source_range = False
            for source_range, offset in mapping.items():
                if source_range[0] <= current < source_range[1]:
                    new_range_len = min(source_range[1] - current, x + n - current)
                    new_ranges.append((current + offset, new_range_len))
                    current += new_range_len
                    found_source_range = True
            if not found_source_range:
                min_overlap = x + n
                for source_range in mapping:
                    if current <= source_range[0] < min_overlap:
                        min_overlap = source_range[0]
                new_ranges.append((current, min_overlap - current))
                current = min_overlap
        return new_ranges
    return map_range

# input_list: list[str]
def solve(input_list):
    seeds = input_list[0].split(": ")[1]
    current_numbers = list(map(lambda x: int(x), seeds.split()))
    current_ranges = list(zip(current_numbers[::2], current_numbers[1::2]))
    current_mapping = dict()
    # This simplifies the for loop ahead
    modified_list = input_list + [""]
    for line in modified_list[3:]:
        if line == "":
            map_number = get_number_map(current_mapping)
            map_range = get_range_map(current_mapping)
            new_ranges = list(map(lambda x: map_range(x[0], x[1]), current_ranges))
            current_ranges = reduce(lambda x, y: x + y, new_ranges)
            current_numbers = list(map(map_number, current_numbers))
            current_mapping = dict()
        elif line[0].isnumeric():
            map_nos = list(map(lambda x: int(x), line.split()))
            current_mapping[(map_nos[1], map_nos[1] + map_nos[2])] = map_nos[0] - map_nos[1]
    return min(current_numbers), min(list(map(lambda x: x[0], current_ranges)))

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")