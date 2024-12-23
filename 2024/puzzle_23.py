from util import *
from collections import defaultdict

def create_graph(edges):
    G = defaultdict(set)
    for e in edges:
        v, w = e.split("-")
        G[v].add(w)
        G[w].add(v)
    return G

# input_list: list[str]
def solve(input_list):
    G = create_graph(input_list)
    cliques = set()
    for v in sorted(G.keys()):
        processed_neighbors = {w for w in G[v] if w < v}
        for c in cliques.copy():
            if all(w in processed_neighbors for w in c):
                cliques.add(c + (v,))
        cliques.add((v,))
    threes_with_ts = [c for c in cliques if len(c) == 3 and any(v.startswith("t") for v in c)]
    return len(threes_with_ts), ",".join(max(cliques, key=lambda x: len(x)))

# Runs in under 5 seconds on my machine
sample_input = get_list_of_strings("sample_input_puzzle_23.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_23.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")