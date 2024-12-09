from util import *

def get_next_to_last_file_index(L, i):
    while L[i] is None:
        i -= 1
    return i

# input_list: list[str]
def solve(input_list):
    blocks, is_file, file_num = [], True, 0
    empty_spaces = {i: [] for i in range(0, 10)}
    file_blocks = dict()
    p1, p2 = 0, 0
    for d in input_list[0]:
        if is_file:
            file_blocks[file_num] = (len(blocks), int(d))
        else:
            empty_spaces[int(d)] += [len(blocks)]
        blocks += [file_num if is_file else None for i in range(int(d))]
        is_file = not is_file
        if is_file:
            file_num += 1
    blocks_2 = blocks.copy()

    last_file_index = get_next_to_last_file_index(blocks, len(blocks) - 1)
    for i in range(len(blocks)):
        if blocks[i] is None and i < last_file_index:
            blocks[i], blocks[last_file_index] = blocks[last_file_index], blocks[i]
            last_file_index = get_next_to_last_file_index(blocks, last_file_index)
        elif blocks[i] is None and i >= last_file_index:
            break
        p1 += i * blocks[i]

    for num in range(file_num, 0, -1):
        orig_i, length = file_blocks[num]
        new_i, gap_len = min(
            [(empty_spaces[l][0] if len(empty_spaces[l]) > 0 else 10 ** 10, l)
                for l in empty_spaces if l >= length],
            key=lambda x: x[0]
        )
        if new_i > orig_i:
            continue
        for i in range(length):
            blocks_2[new_i + i], blocks_2[orig_i + i] = blocks_2[orig_i + i], blocks_2[new_i + i]
        empty_spaces[gap_len] = empty_spaces[gap_len][1:]
        empty_spaces[gap_len - length] = sorted([new_i + length] + empty_spaces[gap_len - length])
        
    for i, file_num in enumerate(blocks_2):
        p2 += i * file_num if file_num is not None else 0

    return p1, p2

sample_input = get_list_of_strings("sample_input_puzzle_9.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_9.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")