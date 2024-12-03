from util import *
from math import gcd
from functools import reduce

# Comment this out if skipping testing on sample input
sample_input_p1 = get_list_of_strings("sample_input_puzzle_8_p1.txt")
sample_input_p2 = get_list_of_strings("sample_input_puzzle_8_p2.txt")
input = get_list_of_strings("input_puzzle_8.txt")

# We'll just represent the graph with a dict here, nothing fancy
def get_graph(adjacencies):
    graph = dict()
    for node_adjacancies in adjacencies:
        source_node, adjacent_nodes = node_adjacancies.split(" = ")
        adj_L, adj_R = adjacent_nodes.replace("(", "").replace(")","").split(", ")
        graph[source_node] = (adj_L, adj_R)
    return graph

def traverse(graph, node, instructions, instruction_index):
    instruction = instructions[instruction_index]
    adjacent_nodes = graph[node]
    new_node = adjacent_nodes[0] if instruction == "L" else adjacent_nodes[1]
    return new_node, (instruction_index + 1) % len(instructions)

# input_list: list[str]
def part_one(input_list):
    instructions = input_list[0]
    graph = get_graph(input_list[2:])
    instr_index, curr_node = 0, "AAA"
    steps = 0
    while curr_node != "ZZZ":
        curr_node, instr_index = traverse(graph, curr_node, instructions, instr_index)
        steps += 1
    return steps

# The repeat length could be different than the length to the first Z. One such
# case is provided in the example for part two: 22A -> 22B -> 22C -> 22Z, so 3
# to get to a Z, but the instructions have length 2 so 6 until a true repeat.
# But in general the repeat length doesn't even have to be related to the
# length to the first Z. For example, A: (B, C), B: (C, A), C:(A, B) LRLRRR,
# starting at node A arrives at node B after steps 1, 3, 6, 8, 10, and 17, with
# a repeat length of 18
def find_repeat_length(graph, instructions, node):
    instr_index, curr_node = 0, node
    states_visited = {(node, 0): 0}
    steps = 0
    while True:
        curr_node, instr_index = traverse(graph, curr_node, instructions, instr_index)
        steps += 1
        current_state = (curr_node, instr_index)
        if current_state in states_visited:
            return steps - states_visited[current_state], steps
        states_visited[current_state] = steps

def confirm_constant_lengths_between_Zs(graph, instructions, node, length_to_Z):
    repeat_length, first_repeat = find_repeat_length(graph, instructions, node)
    assert(repeat_length % length_to_Z == 0)
    if repeat_length != length_to_Z:
        instr_index, curr_node = 0, node
        for i in range(repeat_length // length_to_Z - 1):
            for j in range(length_to_Z):
                curr_node, instr_index = traverse(graph, curr_node, instructions, instr_index)
            assert(curr_node.endswith("Z"))
    assert(first_repeat < 2 * repeat_length)

# This algorithm makes a major simplifying assumption. For an arbitrary
# starting point, let n be the number of traversals until the first time it
# arrives at a node ending in Z. Then after m traversals starting at that
# starting point, this new node ends with a Z if and only f m mod n = 0. This
# is false in general, but for the sample input and input here it happens to
# work. confirm_constant_lengths_between_Zs verifies this property
def part_two(input_list):
    instructions = input_list[0]
    graph = get_graph(input_list[2:])
    nodes = []
    for node in graph:
        if node.endswith("A"):
            nodes.append(node)
    lengths_to_Z = []
    for node in nodes:
        instr_index, curr_node = 0, node
        steps = 0
        while not curr_node.endswith("Z"):
            curr_node, instr_index = traverse(graph, curr_node, instructions, instr_index)
            steps += 1
        confirm_constant_lengths_between_Zs(graph, instructions, node, steps)
        lengths_to_Z.append(steps)
    # Take the LCM of the cycle lengths
    return reduce(lambda x, y: x * y // gcd(x, y), lengths_to_Z)

# Part 1
print(f"Part 1 answer for sample input: {part_one(sample_input_p1)}")
print(f"Part 1 final answer: {part_one(input)}")

# Part 2 
print(f"Part 2 answer for sample input: {part_two(sample_input_p2)}")
print(f"Part 2 final answer: {part_two(input)}")