from util import *

OPERATIONS = {
    "OR": "|",
    "AND": "&",
    "XOR": "^",
}

def parse_input(input):
    values = dict()
    for initial_value in input[0]:
        var, val = initial_value.split(": ")
        values[var] = val
    for computation in input[1]:
        expression, var = computation.split(" -> ")
        values[var] = expression
    return values

def compute_value(values, var):
    if values[var] in "01":
        return values[var]
    ref1, op, ref2 = values[var].split(" ")
    res1, res2 = compute_value(values, ref1), compute_value(values, ref2)
    op_string = OPERATIONS[op]
    values[var] = str(eval(res1 + op_string + res2))
    return values[var]

def set_initial_values(values, x, y):
    for n in range(45):
        end = str(n) if n >= 10 else "0" + str(n)
        values["x" + end] = str(x % 2)
        values["y" + end] = str(y % 2)
        x, y = x //2, y // 2

def get_supposed_sum(values):
    z_values = dict()
    for k in values:
        compute_value(values, k)
        if k.startswith("z"):
            z_values[int(k[1:])] = values[k]
    result = ""
    for n in sorted(z_values.keys()):
        result = z_values[n] + result
    return int(result, 2)

# For part 2 today, I used the for loop below to find the first time the addition broke down
# To actually accomplish addition, you need equations of this form:
# z_n = a_n xor b_n, where:
# a_n = x_n xor y_n, b_n = c_n or d_n, c_n = x_{n - 1} and y_{n - 1}, d_n = a_{n - 1} and b_{n - 1}
# From there I, by hand, looked at what was wrong, hardcoded the swap, and looked at the next
# problem. This would be messy to automate, so I'm forgoing it. Let's make an extra assumptions
# about the input which was true in my case: for each n, at most one of the variables involved in
# the equations above is mislabeled. In that case, we could just find the first n where there's a 
# problem, and try all 200 some choose 2 swaps until we found the one that fixed the issue, and
# then keep going
# input_list: list[str]
def solve(input_list):
    values = parse_input(input_list)
    p1 = get_supposed_sum(values)
    values = parse_input(input_list)
    for i in range(45):
        values = parse_input(input_list)
        set_initial_values(values, 1, 2 ** i - 1)
        if not 2 ** i == get_supposed_sum(values):
            print(i)
            break
    return p1, None

sample_input = get_list_of_strings("sample_input_puzzle_24.txt", line_break="\n\n")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_24.txt", line_break="\n\n")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")