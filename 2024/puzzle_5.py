from util import *

def order_pages(L, lt):
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if not lt(L[j], L[j + 1]):
                L[j], L[j + 1] = L[j + 1], L[j]

# input_list: list[str]
def solve(input_list):
    S = set(input_list[0])
    def lt(a, b):
        return f"{a}|{b}" in S
    updates = [line.split(",") for line in input_list[1]]
    p1, p2 = 0, 0 
    for L in updates:
        if all([lt(L[i], L[j]) for j in range(len(L)) for i in range(j)]):
            p1 += int(L[len(L) // 2])
        else:
            order_pages(L, lt)
            p2 += int(L[len(L) // 2])
    return p1, p2

sample_input = get_list_of_strings("sample_input_puzzle_5.txt", line_break="\n\n")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_5.txt", line_break="\n\n")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")