from util import *

def parse_machine(machine):
    machine_ints = [
        (int(x_s[x_s.find("X") + 2:]), int(y_s[y_s.find("Y") + 2:])) for x_s, y_s in machine
    ]
    return machine_ints[0] + machine_ints[1], machine_ints[2]

def solve_eqn(M, v):
    # Swap the middle entries for the matrix equation to be correct
    a, c, b, d = M
    x, y = v
    # I checked to make sure that det != 0 is always true
    det = a * d - b * c
    a_pushes, b_pushes = d*x - b*y, a*y - c*x
    # We can only push buttons an integer number of times
    if not (a_pushes % det == 0 and b_pushes % det == 0):
        return 0
    # Part 1 says we'll always have 0 <= pushes <= 100, so we don't need to check this
    a_pushes, b_pushes = a_pushes // det, b_pushes // det
    return 3 * a_pushes + b_pushes

# input_list: list[str]
def solve(input_list):
    machines = [parse_machine(machine) for machine in input_list]
    return (
        sum([solve_eqn(M, v) for M, v in machines]),
        sum([solve_eqn(M, add_tuples(v, (10000000000000, 10000000000000))) for M, v in machines]),
    )

sample_input = get_list_of_strings("sample_input_puzzle_13.txt", line_break="\n\n", separation=",")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_13.txt", line_break="\n\n", separation=",")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")