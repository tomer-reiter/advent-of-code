from util import *

# input_list: list[str]
def solve(input_list):
    l1, l2 = [int(line[0]) for line in input_list], [int(line[1]) for line in input_list]
    l1.sort(), l2.sort()
    sums = combine_tuples(l1, l2, lambda x,y: x - y)
    l1_similarities = [num * l1.count(num) for num in l1]
    return sum([abs(s) for s in sums]), sum(l1_similarities)

sample_input = get_list_of_strings("sample_input_puzzle_1.txt", separation="   ")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_1.txt", separation="   ")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")