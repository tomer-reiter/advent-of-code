from util import *

# I did end up needing to peek at the AoC Reddit to get a nudge that there was something special
# about the input. The print statement on line 19 is never reached, so this code is enough
# input_list: list[str]
def solve(input_list):
    sizes = []
    for i in range(6):
        sizes.append(sum([l.count("#") for l in input_list[i][1:]]))
    total_possible = 0
    for region in input_list[-1]:
        dims, counts = region.split(": ")
        dims = [int(d) for d in dims.split("x")]
        counts = [int(c) for c in counts.split(" ")]
        present_area = sum([counts[i] * sizes[i] for i in range(6)])
        if present_area > int(dims[0]) * int(dims[1]):
            continue
        if (dims[0] // 3) * (dims[1] // 3) < sum(counts):
            print(f"Line for further analysis: {region}")
        total_possible += 1
    return total_possible

input = get_list_of_strings("input_puzzle_12.txt", line_break="\n\n")
p1 = solve(input)
print(f"Part 1 final answer: {p1}")