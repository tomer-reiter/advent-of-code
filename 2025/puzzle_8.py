from util import *

def dist(e, verts):
    return sum([(int(verts[e[0]][k]) - int(verts[e[1]][k])) ** 2 for k in range(3)])

# input_list: list[str]
def solve(input_list, conns):
    edges = [(i, j) for i in range(len(input_list)) for j in range(i + 1, len(input_list))]
    edges = sorted(edges, key=lambda e: dist(e, input_list))
    components = {i: set([i]) for i in range(len(input_list))}
    conn_count = 0
    for e in edges:
        conn_count += 1
        if e[0] in components[e[1]]:
            continue
        new_comp = components[e[0]].union(components[e[1]])
        if len(new_comp) == len(input_list):
            return p1, int(input_list[e[0]][0]) * int(input_list[e[1]][0])
        for v in new_comp:
            components[v] = new_comp
        if conn_count == conns:
            sizes = sorted([len(components[v]) for v in range(len(input_list))], reverse=True)
            p1 = sizes[0] * sizes[sizes[0]] * sizes[sizes[sizes[0]] + sizes[0]]

sample_input = get_list_of_strings("sample_input_puzzle_8.txt", separation=",")
sample_p1, sample_p2 = solve(sample_input, 10)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_8.txt", separation=",")
p1, p2 = solve(input, 1000)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")