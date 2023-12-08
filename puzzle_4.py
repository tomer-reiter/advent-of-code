from util import *

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_4.txt")
input = get_list_of_strings("input_puzzle_4.txt")

# input_list: list[str]
def solve(input_list):
    p1 = 0
    p2 = 0
    cards = {0: 1}
    for i, line in enumerate(input_list):
        cards[i] = cards.get(i, 1)
        p2 += cards[i]
        numbers = line.split(": ")[1]
        winning_numbers, your_numbers = numbers.split(" | ")
        winning_numbers = set(map(lambda s: int(s), winning_numbers.split()))
        your_numbers = list(map(lambda s: int(s), your_numbers.split()))
        your_winners = 0
        for number in your_numbers:
            if number in winning_numbers:
                your_winners += 1
        p1 = p1 + 2 ** (your_winners - 1) if your_winners > 0 else p1
        for j in range(your_winners):
            cards[i + j + 1] = cards.get(i + j + 1, 1) + cards[i]
    return p1, p2

sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")