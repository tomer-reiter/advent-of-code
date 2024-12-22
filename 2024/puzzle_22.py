from util import *

def next_secret(secret):
    secret = ((secret * 64) ^ secret) % 16777216
    secret = (secret // 32) ^ secret
    return ((secret * 2048) ^ secret) % 16777216

# input_list: list[str]
def solve(input_list):
    total = 0
    earnings = dict()
    for n in input_list:
        n = int(n)
        seen = set()
        recent = tuple()
        for _ in range(2000):
            next = next_secret(n)
            recent = recent[-3:] + (((next % 10) - n % 10),)
            if len(recent) == 4 and not recent in seen:
                seen.add(recent)
                earnings[recent] = earnings.get(recent, 0) + (next % 10)
            n = next
        total += n
    return total, earnings[max(earnings, key=earnings.get)]

sample_input = get_list_of_strings("sample_input_puzzle_22.txt")
sample_p1, sample_p2 = solve(sample_input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 2 answer for sample input: {sample_p2}")

input = get_list_of_strings("input_puzzle_22.txt")
p1, p2 = solve(input)
print(f"Part 1 final answer: {p1}")
print(f"Part 2 final answer: {p2}")