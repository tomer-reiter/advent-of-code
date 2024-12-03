from util import *
import math
from collections import deque

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_20.txt")
input = get_list_of_strings("input_puzzle_20.txt")

def create_state_and_module_configuration_objects(input_list):
    states, config = dict(), dict()
    for line in input_list:
        module, destinations = line.split(" -> ")
        if module == "broadcaster":
            config["B"] = destinations.split(", ")
        else:
            label = module[1:]
            config[label] = destinations.split(", ")
            states[label] = ["%", 0] if module[0] == "%" else ["&", dict()]
    for label, destinations in config.items():
        for destination in destinations:
            state = states.get(destination, ("."))
            if state[0] == "&":
                state[1][label] = 0
    return config, states

def get_signals(dest, signal, orig, config, states):
    if dest not in config:
        return []
    elif dest == "B":
        return [(new_dest, 0, dest) for new_dest in config[dest]]
    state = states[dest]
    new_signal = None
    if state[0] == "%" and signal == 0:
        state[1] = 1 - state[1]
        new_signal = state[1]
    elif state[0] == "&":
        state[1][orig] = signal
        new_signal = 1 - math.prod(state[1].values())
    if new_signal is not None:
        return [(new_dest, new_signal, dest) for new_dest in config[dest]]
    else:
        return []
        

def push_button(config, states, cycle_lengths, pushes):
    queue = deque([("B", 0, "")])
    pulse_counts = [0, 0]
    while len(queue) > 0:
        dest, signal, orig = queue.popleft()
        # Cycle lengths is logic for part two
        if cycle_lengths.get(orig) == 0 and signal == 0:
            cycle_lengths[orig] = pushes
        # Pulse counts is logic for part one
        pulse_counts[signal] += 1
        for new_entry in get_signals(dest, signal, orig, config, states):
            queue.append(new_entry)
    return pulse_counts

# input_list: list[str]
def part_one(input_list):
    config, states = create_state_and_module_configuration_objects(input_list)
    pulse_totals = (0, 0)
    for i in range(1000):
        pulse_totals = add_tuples(push_button(config, states, dict(), i + 1), pulse_totals)
    return pulse_totals[0]*pulse_totals[1]

# This only works because of the structure of the input. There are four
# conjuction modules, each pointing to an inverter. The four inverters all
# point to one final conjuction module, which points to the destination, rx.
# There are no other conjuctions or dependencies among them. So we for each of
# the original four conjuction modules, there will by some cycle length such
# that after pushing by any multiple of that cycle length, it will send a 1. 
def part_two(input_list):
    pushes = 0
    config, states = create_state_and_module_configuration_objects(input_list)
    cycle_lengths = {label: 0 for label in ["gr", "vc", "db", "lz"]}
    while math.prod(cycle_lengths.values()) == 0:
        pushes += 1
        push_button(config, states, cycle_lengths, pushes)
    return math.prod(cycle_lengths.values())

# Runs in about .3 seconds on my machine
# Part 1
print(f"Part 1 answer for sample input: {part_one(sample_input)}")
print(f"Part 1 final answer: {part_one(input)}")

# Part 2 
print(f"Part 2 final answer: {part_two(input)}")