from util import *
from itertools import product
from functools import cache

numpad = ["789", "456", "123", ".0A"]
keypad = [".^A", "<v>"]

def is_valid_move(pad, c, move):
    for d in move:
        c = add_tuples(c, DIRECTION_VECTORS[d])
        if pad[c[0]][c[1]] == ".":
            return False
    return True

def generate_moves(pad):
    possible_coords = list(product(range(len(pad)), range(len(pad[0]))))
    moves = dict()
    for c1, c2 in product(possible_coords, possible_coords):
        x_diff = c2[0] - c1[0]
        move_ud = ("v" if x_diff > 0 else "^") * abs(x_diff)
        y_diff = c2[1] - c1[1]
        move_lr = (">" if y_diff > 0 else "<") * abs(y_diff)
        possible_moves = [move_ud + move_lr, move_lr + move_ud]
        valid_moves = [move + "A" for move in possible_moves if is_valid_move(pad, c1, move)]
        moves[pad[c1[0]][c1[1]] + pad[c2[0]][c2[1]]] = list(set(valid_moves))
    return moves

numpad_moves = generate_moves(numpad)
keypad_moves = generate_moves(keypad)

# Note, we are a robot
@cache
def min_moves(robots_left, total_robots, transition):
    # This is a bit of a trick: when robots_left == 1, we'll have be recursively testing, say
    # <<A, by calling min_moves on each of A<, <<, <A, which happens to be the length of <<A
    if robots_left == 0:
        return 1
    pad_moves = numpad_moves if robots_left == total_robots else keypad_moves
    min_moves_from_here = [
        sum([min_moves(robots_left - 1, total_robots, ("A" + move)[i: i + 2]) 
             for i in range(len(move))])
        for move in pad_moves[transition]
    ]
    return min(min_moves_from_here)

def get_complexity(num_robots, codes):
    total_complexity = 0
    for code in codes:
        shortest_len = sum(
            [min_moves(num_robots, num_robots, ("A" + code)[i: i + 2]) for i in range(len(code))]
        )
        total_complexity += shortest_len * int(code[:-1])
    return total_complexity

# input_list: list[str]
def solve(input_list):
    return get_complexity(3, input_list), get_complexity(26, input_list)

sample_input = get_list_of_strings("sample_input_puzzle_21.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_21.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")