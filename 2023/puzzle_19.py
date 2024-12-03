from util import *
import math
import copy

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_19.txt", "\n\n")
input = get_list_of_strings("input_puzzle_19.txt", "\n\n")

def get_workflow_function(workflow):
    def workflow_function(xmas):
        x, m, a, s = xmas
        expressions = workflow.split(",")
        for expression in expressions:
            if not ":" in expression:
                return expression
            if eval(expression.split(":")[0]):
                return expression.split(":")[1]
    return workflow_function

def intersect_intervals(i1, i2):
    return max(i1[0], i2[0]), min(i1[1], i2[1])

def count_possibilities(workflows_object, label, xmas):
    if label == "A":
        return math.prod(map(lambda T: T[1] - T[0], xmas))
    elif label == "R":
        return 0
    workflow = workflows_object[label]
    remaining = xmas
    possibilities = 0
    for rule in workflow.split(","):
        if not ":" in rule:
            possibilities += count_possibilities(workflows_object, rule, remaining)
            break
        else:
            inequality, new_label = rule.split(":")
            passed_xmas = copy.copy(remaining)
            xmas_i = "xmas".find(inequality[0])
            n = int(inequality[2:])
            passed_interval = (1, n) if inequality[1] == "<" else (n + 1, 4001)
            failed_interval = (n, 4001) if inequality[1] == "<" else (1, n + 1)
            passed_xmas[xmas_i] = intersect_intervals(passed_interval, remaining[xmas_i])
            remaining[xmas_i] = intersect_intervals(failed_interval, remaining[xmas_i])
            possibilities += count_possibilities(workflows_object, new_label, passed_xmas)
    return possibilities

# input_list: list[str]
def solve(input_list):
    workflows, parts = input_list
    workflows_object = dict()
    for line in workflows:
        label, workflow = line.split("{")
        workflow = workflow.replace("}", "")
        workflows_object[label] = get_workflow_function(workflow)
    p1 = 0
    for part in parts:
        label = "in"
        xmas = ("".join(filter(lambda c: c.isnumeric() or c == ",", part))).split(",")
        xmas = list(map(lambda s: int(s), xmas))
        while not label in "AR":
            label = workflows_object[label](xmas)
        if label == "A":
            p1 += sum(xmas)
    p2_workflows_object = dict()
    for line in workflows:
        label, workflow = line.split("{")
        workflow = workflow.replace("}", "")
        p2_workflows_object[label] = workflow
    p2 = count_possibilities(workflows_object, "in", [(1, 4001) for i in range(4)])
    return p1, p2

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")