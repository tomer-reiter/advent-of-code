from util import *

def mul(s):
    c_index, p_index = s.find(","), s.find(")")
    if not (0 < c_index < p_index < 8 and 2 <= p_index - c_index <= 4 and c_index <= 3):
        return 0
    n1, n2 = s[:c_index], s[c_index + 1: p_index]
    if not (n1.isnumeric() and n2.isnumeric()):
        return 0
    return int(n1) * int(n2)

def get_next_indices(s):
    return {keyword: s.find(keyword) for keyword in ["mul(", "do()", "don't()"] if s.find(keyword) != -1}

# input_list: list[str]
def solve(input_list):
    line = " ".join(input_list)
    do, p1_total, p2_total = True, 0, 0
    next_indices = get_next_indices(line)
    while "mul(" in next_indices:
        next_command= min(next_indices, key=next_indices.get)
        next_index = next_indices[next_command]
        line = line[next_index + len(next_command):]
        if next_command == "mul(":
            p1_total += mul(line)
            p2_total += mul(line) if do else 0
        else:
            do = next_command == "do()"
        next_indices = get_next_indices(line)
    return p1_total, p2_total

sample_input = get_list_of_strings("sample_input_puzzle_3.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_3.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")