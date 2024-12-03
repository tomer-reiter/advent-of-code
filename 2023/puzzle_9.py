from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_9.txt")
input = get_list_of_strings("input_puzzle_9.txt")

def predict_next(sequence):
    deltas = sequence
    next = 0
    while not (len(set(deltas)) == 1 and deltas[0] == 0):
        next += deltas[-1]
        deltas = [deltas[i+1] - deltas[i] for i in range(len(deltas) - 1)]
    return next

# input_list: list[str]
def solve(input_list):
    p1 = 0
    p2 = 0
    for line in input_list:
        deltas = list(map(lambda x: int(x), line.split()))
        p2_deltas = deltas[::-1]
        p1 += predict_next(deltas)
        p2 += predict_next(p2_deltas)
    return p1, p2


sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")