from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_14.txt")
input = get_list_of_strings("input_puzzle_14.txt")

def get_rock_and_object_locations(input_list):
    object_locations = dict()
    rock_locations = set()
    for i in range(len(input_list)):
        for j in range(len(input_list[0])):
            if input_list[i][j] != ".":
                object_locations[i] = object_locations.get(i, []) + [j]
            if input_list[i][j] == "#":
                rock_locations.add((i, j))
    return object_locations, rock_locations

def transpose(object_locations, n):
    transposed = dict()
    for i in range(n):
        for j in object_locations.get(i, []):
            transposed[j] = transposed.get(j, []) + [i]
    return transposed

# The idea here is to store locations per line in a list, then go through
# that list one by one moving up each one as far as it can go
def move_rocks(object_locations, rock_locations, n, dir):
    locations = transpose(object_locations, n) if dir in "NS" else object_locations
    for i, js in locations.items():
        max_available = n
        for k in range(len(js)):
            js_index = k if dir in "NW" else len(js) - k - 1
            j = js[js_index]
            possible_rock = (j, i) if dir in "NS" else (i, j)
            if possible_rock in rock_locations:
                max_available = n - j - 1 if dir in "NW" else j
            else:
                js[js_index] = n - max_available if dir in "NW" else max_available - 1 
                max_available -= 1
    return transpose(locations, n) if dir in "NS" else locations

def get_hashable_locations(locations, n):
    s = ""
    for i in range(n):
        s += "r" + str(i)
        s += "".join("c" + str(j) for j in locations.get(i, []))
    return s

def count_north_load(object_locations, rock_locations, n):
    load = 0
    for i, js in object_locations.items():
        load += sum(1 for j in js if not (i, j) in rock_locations) * (n - i)
    return load

# input_list: list[str]
def solve(input_list):
    object_locations, rock_locations = get_rock_and_object_locations(input_list)
    n = len(input_list)
    cycles = 0
    seen, north_loads = dict(), dict()
    target_cycle = 1000000000
    cycles_cycle_found = False
    while not cycles_cycle_found:
        for dir in "NWSE":
            object_locations = move_rocks(object_locations, rock_locations, n, dir)
            if cycles == 1 and dir == "N":
                p1 = count_north_load(object_locations, rock_locations, n)
        cycles += 1
        hashable_locations = get_hashable_locations(object_locations, n)
        if hashable_locations in seen:
            prev_cycle = seen[hashable_locations]
            cycles_cycle_found = True
            target_cycle = prev_cycle + ((target_cycle - prev_cycle) % (cycles - prev_cycle))
        else:
            seen[hashable_locations] = cycles
            north_loads[cycles] = count_north_load(object_locations, rock_locations, n)
    return p1, north_loads[target_cycle]

# Runs in just under 1.2 seconds on my machine
sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")