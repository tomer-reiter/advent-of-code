from util import *
from functools import reduce

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_15.txt")
input = get_list_of_strings("input_puzzle_15.txt")

def get_hash(s):
    # Add a 0 to multiply by 17 at the end too
    ascii_values = list(map(lambda x: ord(x), s)) + [0]
    return reduce(lambda x, y: (17*x + y) % 256, ascii_values)

# input_list: list[str]
def solve(input_list):
    steps = input_list[0].split(",")
    p1 = sum(map(get_hash, steps))
    focal_lengths, boxes = dict(), dict()
    for step in steps:
        is_dash_operation = step[-1] == "-"
        label = step[:-1] if is_dash_operation else step[:-2]
        if is_dash_operation and label in focal_lengths:
            hash = get_hash(label)
            del focal_lengths[label]
            boxes[hash].remove(label)
        elif not is_dash_operation:
            focal_length = int(step[-1])
            if not label in focal_lengths:
                hash = get_hash(label)
                boxes[hash] = boxes.get(hash, []) + [label]
            focal_lengths[label] = focal_length
    p2 = 0
    for box_no, labels in boxes.items():
        p2 += (box_no + 1) * sum((i + 1) * focal_lengths[labels[i]] for i in range(len(labels)))
    return p1, p2

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")