from util import *

# input_list: list[str]
def solve(input_list):
    invalid_ids, more_invalid_ids = set(), set()
    for rng in input_list[0]:
        lower, upper = rng.split("-")
        for reps in range(2, len(upper) + 1):
            s = lower[:len(lower)//reps]
            if reps * len(s) != len(lower):
                s = "1" + ("0" * len(s))
            elif int(reps * s) < int(lower):
                s = str(int(s) + 1)
            while int(reps * s) <= int(upper):
                if reps == 2:
                    invalid_ids.add(int(reps * s))
                more_invalid_ids.add(int(reps * s))
                s = str(int(s) + 1)
    return sum(invalid_ids), sum(more_invalid_ids)

sample_input = get_list_of_strings("sample_input_puzzle_2.txt",separation=",")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_2.txt",separation=",")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")