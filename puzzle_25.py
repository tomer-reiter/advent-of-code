from util import *
import copy
import random

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_25.txt")
input = get_list_of_strings("input_puzzle_25.txt")

def get_graph(connections):
    graph = dict()
    for connection in connections:
        node, neighbors = connection.split(": ")
        neighbors = neighbors.split()
        graph[node] = graph.get(node, []) + neighbors
        for neighbor in neighbors:
            graph[neighbor] = graph.get(neighbor, []) + [node]
    return graph

def contract_edge(G, v1, v2):
    new_G = dict()
    for v in G:
        if v != v2:
            new_G[v] = G[v]
        if v != v2:
            while v2 in new_G[v]:
                new_G[v].remove(v2)
    for neighbor in G[v2]:
        if neighbor != v1:
            new_G[v1].append(neighbor)
            new_G[neighbor].append(v1)
    return new_G

# This is an implementation of Karger's algorithm. The idea is, pick an edge
# at random and contract it. Repeat this until 2 vertices remain, and the
# number of edges between them is a cut of the graph. Since we know the min cut
# of this graph is 3, we repeat until we find a cut of size 3
def karger(G):
    new_G = copy.deepcopy(G)
    component_counts = {v: 1 for v in new_G}
    while len(new_G) > 2:
        # This is technically not the same probability space as picking a
        # random edge, but I don't keep track of the edge set here and this is
        # close enough
        v1, neighbors = random.sample(new_G.items(), 1)[0]
        v2 = random.sample(neighbors, 1)[0]
        new_G = contract_edge(new_G, v1, v2)
        component_counts[v1] = component_counts[v1] + component_counts[v2]
    prod = 1
    for v in new_G:
        if len(new_G[v]) != 3:
            return None
        prod *= component_counts[v]
    return prod

# input_list: list[str]
def solve(input_list):
    graph = get_graph(input_list)
    min_cut_prod = karger(graph)
    while min_cut_prod is None:
        min_cut_prod = karger(graph)
    return min_cut_prod


sample_p1 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
p1 = solve(input)
print(f"Part 1 final answer: {p1}")