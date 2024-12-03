from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_2.txt")
input = get_list_of_strings("input_puzzle_2.txt")

suffix_limits = {
    " red": 12,
    " green": 13,
    " blue": 14,
}

def parse_line(line):
    game, pulls = line.split(": ")
    number = int(game.replace("Game ", ""))
    return number, pulls.split("; ")

# input_list: list[str]
def solve(input_list):
    possible_game_total = 0
    power_total = 0
    for line in input_list:
        valid_pull = True
        min_cubes = {" red": 0, " blue": 0, " green": 0}
        game_number, pulls = parse_line(line)
        for pull in pulls:
            for cubes in pull.split(", "):
                cubes_copy = cubes
                for suffix, limit in suffix_limits.items():
                    if cubes.endswith(suffix):
                        valid_pull = valid_pull and int(cubes_copy.replace(suffix, "")) <= limit
                        min_cubes[suffix] = max(min_cubes[suffix], int(cubes_copy.replace(suffix, "")))
        if valid_pull:
            possible_game_total += game_number
        power_total += min_cubes[" red"] * min_cubes[" blue"] * min_cubes[" green"]
    return possible_game_total, power_total

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")