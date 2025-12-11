from util import *

# input_list: list[str]
def solve_p1(input_list):
    G = {line[0]: line[1].split(" ") for line in input_list}
    path_count = {"you": 1}
    out_count = 0
    while len(path_count) > 0:
        new_path_count = dict()
        for v in path_count:
            for w in G[v]:
                if w == "out":
                    out_count += path_count[v]
                else:
                    new_path_count[w] = new_path_count.get(w, 0) + path_count[v]
        path_count = new_path_count
    return out_count

# input_list: list[str]
def solve_p2(input_list):
    G = {line[0]: line[1].split(" ") for line in input_list}
    # Tuple represents # of paths that go through: None, dac, fft, both
    path_count = {"svr": (1, 0, 0, 0)}
    out_count = 0
    while len(path_count) > 0:
        new_path_count = dict()
        for v in path_count:
            for w in G[v]:
                if w == "out":
                    out_count += path_count[v][3]
                    continue
                to_add = path_count[v]
                if w == "dac":
                    to_add = (0, to_add[0] + to_add[1], 0, to_add[2] + to_add[3])
                elif w == "fft":
                    to_add = (0, 0, to_add[0] + to_add[2], to_add[1] + to_add[3])
                new_path_count[w] = add_tuples(new_path_count.get(w, (0, 0, 0, 0)), to_add)
        path_count = new_path_count
    return out_count

sample_input = get_list_of_strings("sample_input_puzzle_11.txt", separation=": ")
sample_p1, sample_p2 = solve_p1(sample_input), solve_p2(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_11.txt", separation=": ")
p1, p2 = solve_p1(input), solve_p2(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")