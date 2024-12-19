from util import *

def count_patterns(pattern, towels, biggest_towel, results):
    if pattern in results:
        return results[pattern]
    results[pattern] = sum([
        count_patterns(pattern[i + 1:], towels, biggest_towel, results)
        for i in range(biggest_towel) if pattern[:i + 1] in towels and i + 1 <= len(pattern)
    ])
    return results[pattern]

# input_list: list[str]
def solve(input_list):
    towels, patterns = input_list
    towels = set(towels[0].split(", "))
    biggest_towel = max([len(t) for t in towels])
    results = {"": 1}
    counts = [count_patterns(pattern, towels, biggest_towel, results) for pattern in patterns]
    return len([n for n in counts if n > 0]), sum(counts)

sample_input = get_list_of_strings("sample_input_puzzle_19.txt", line_break="\n\n")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_19.txt", line_break="\n\n")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")