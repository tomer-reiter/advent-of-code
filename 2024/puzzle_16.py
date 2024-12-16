from util import *
from itertools import product

DIRS = "^>v<"

# This makes the grid into a graph: vertices occur where one could turn non-trivially,
# i.e. not 180 degrees, and some extra for the start and end vertices. The data structure
# here is a dictionary mapping v -> edges(v), where v is a vertex ((row, col), direction),
# and edges(v) is a dictionary mapping w -> dist(v, w), for neighbors w of v
def process_grid(grid):
    vertices = dict()
    end = set()
    for p in product(range(len(grid)), range(len(grid[0]))):
        sym = grid[p[0]][p[1]]
        if sym in "SE":
            for i in range(4):
                adj = add_tuples(p, DIRECTION_VECTORS[DIRS[i]])
                if sym == "S" and (grid[adj[0]][adj[1]] == "." or i == 1):
                    start = (p, 1)
                    vertices[(p, i)] = dict()
                elif sym == "E" and grid[adj[0]][adj[1]] == ".":
                    vertices[(p, (i + 2) % 4)] = dict()
                    end.add((p, (i + 2) % 4))
        elif sym == ".":
            valid_dirs = []
            for i in range(4):
                adj = add_tuples(p, DIRECTION_VECTORS[DIRS[i]])
                if grid[adj[0]][adj[1]] == ".":
                    valid_dirs += [i]
            # If we're not just at a straightaway
            if (len(valid_dirs) >= 3 or 
                (len(valid_dirs) == 2 and (valid_dirs[1] - valid_dirs[0] % 4) != 2)):
                for i in range(4):
                    vertices[(p, i)] = dict()
    # Add rotation options
    for p, i in vertices:
        for i_orth in [(i + 1) % 4, (i - 1) % 4]:
            if (p, i_orth) in vertices:
                vertices[(p, i)][(p, i_orth)] = 1000
    # Add go straight options
    for p, i in vertices:
        current = p
        vertex_found, wall_found = False, False
        dist = 0
        while not (vertex_found or wall_found):
            current = add_tuples(current, DIRECTION_VECTORS[DIRS[i]])
            dist += 1
            if grid[current[0]][current[1]] == "#":
                wall_found = True
            elif (current, i) in vertices:
                vertex_found = True
        if vertex_found:
            vertices[(p, i)][(current, i)] = dist
    return vertices, start, end

# This is Dijkstra's algorithm, modified to keep track of all min paths
# I'm not using a heap here, but the code runs in a split second so there was no need
def shortest_paths(vertices, start, end):
    distances = {v: (0, set()) if v == start else (10 ** 10, set()) for v in vertices}
    boundary, visited = set([start]), set()
    while not all([v in visited or v in boundary for v in end]):
        closest_v = min(boundary, key=lambda v: distances[v][0])
        for w in vertices[closest_v]:
            if w not in visited:
                dist_to_w = distances[closest_v][0] + vertices[closest_v][w]
                if dist_to_w < distances[w][0]:
                    distances[w] = (dist_to_w, set([closest_v]))
                elif dist_to_w == distances[w][0]:
                    distances[w][1].add(closest_v)
                boundary.add(w)
        visited.add(closest_v)
        boundary.remove(closest_v)
    return distances

# input_list: list[str]
def solve(input_list):
    vertices, start, end = process_grid(input_list)
    distances = shortest_paths(vertices, start, end)
    p1 = min([distances[v][0] for v in end])
    sitting_spots = set()
    to_process = [v for v in end if distances[v][0] == p1]
    while len(to_process) > 0:
        v = to_process[0]
        for w in distances[v][1]:
            delta = combine_tuples(v[0], w[0], lambda a, b: a - b)
            dist = abs(sum(delta)) # This is now grid distance, instead of graph distance
            delta = (delta[0] // dist, delta[1] // dist) if dist != 0 else (0, 0)
            for i in range(dist + 1):
                sitting_spots.add(add_tuples(w[0], scalar_multiply(i, delta)))
            if w != start:
                to_process.append(w)
        to_process.pop(0)
    return p1, len(sitting_spots)

sample_input = get_list_of_strings("sample_input_puzzle_16.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_16.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")