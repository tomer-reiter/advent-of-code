from util import *

def process_machine(machine):
    lights_goal = machine[0][1:-1]
    buttons = []
    for button in machine[1:-1]:
        buttons.append([int(d) for d in button[1:-1].split(",")])
    return lights_goal, buttons

def get_min_presses(machine):
    lights_goal, buttons = process_machine(machine)
    min_presses = len(lights_goal)
    for i in range(2 ** len(buttons)):
        binary = "0" * (len(buttons) - len(bin(i)) + 2) + bin(i)[2:]
        lights = [0 for _ in range(len(lights_goal))]
        for j in range(len(binary)):
            if binary[j] == "0":
                continue
            button = [1 if k in buttons[j] else 0 for k in range(len(lights_goal))]
            lights = add_tuples(lights, button)
        lights_string = "".join(["#" if lights[k] % 2 == 1 else "." for k in range(len(lights))])
        if lights_string == lights_goal:
            min_presses = min(min_presses, binary.count("1"))
    return min_presses


# input_list: list[str]
def solve(input_list):
    return sum([get_min_presses(machine) for machine in input_list]), None

# I ended up using Sage math for part 2. Here's the code, replacing {{ INPUT_FILE_CONTENTS }}
# appropriately. This usess the same process_machine function above, slightly modified to get
# the numbers in the curly braces
# 
# machines = """{{ INPUT_FILE_CONTENTS }}
# """
# machines = [line.split(" ") for line in machines.splitlines()]
# 
# total_presses = 0
# for machine in machines:
#     lights_goal, buttons = process_machine(machine)
#     p = MixedIntegerLinearProgram(maximization=False, solver='GLPK')
#     w = p.new_variable(integer=True, nonnegative=True)
#     for i in range(len(lights_goal)):
#         p.add_constraint(sum([w[j] for j in range(len(buttons)) if i in buttons[j]]) == lights_goal[i])
#     p.set_objective(sum([w[j] for j in range(len(buttons))]))
#     total_presses += int(p.solve())

# print(total_presses)

sample_input = get_list_of_strings("sample_input_puzzle_10.txt", separation=" ")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_10.txt", separation=" ")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")