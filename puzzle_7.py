from util import *
import string

# Comment this out if skipping testing on sample input
sample_input = get_list_of_strings("sample_input_puzzle_7.txt")
input = get_list_of_strings("input_puzzle_7.txt")

cards = "23456789TJQKA"
cards_adjusted = "J23456789TQKA"

# The output function takes a hand to a string where the first few chars
# represent the hand type, e.g. "32..." is a full house. If a hand type beats
# another hand type, that comes up earlier in the lexicographical comparison
# than the remaining chars. E.g. "32gbbgb" > "311ihjii" since 2 > 1
def get_key_fn(adjusted):
    def get_key(h):
        card_counts = dict()
        for card in h:
            card_counts[card] = card_counts.get(card, 0) + 1
        if adjusted and "J" in card_counts:
            J_count = card_counts["J"]
            if J_count != 5:
                del card_counts["J"]
                most_common_card = max(card_counts, key=card_counts.get)
                card_counts[most_common_card] += J_count
        counts = list(card_counts.values())
        counts.sort(reverse=True)
        # Hand ranks are sorted in lexicographical ordering, so we convert 
        # the counts to strings first. i.e. 5 > 4 1 > 3 2 > 3 1 1 ...
        hand_key = "".join(map(lambda x: str(x), counts))
        for c in h:
            value_index = cards_adjusted.index(c) if adjusted else cards.index(c)
            hand_key += string.ascii_lowercase[value_index]
        return hand_key
    return get_key

# input_list: list[str]
def solve(input_list):
    bids = {line.split()[0]: int(line.split()[1]) for line in input_list}
    hands = list(bids.keys())
    sorted_hands = sorted(hands, key=get_key_fn(False))
    adjusted_sorted_hands = sorted(hands, key=get_key_fn(True))
    return (
        sum(bids[hand] * (i + 1) for i, hand in enumerate(sorted_hands)), 
        sum(bids[hand] * (i + 1) for i, hand in enumerate(adjusted_sorted_hands))
    )


sample_p1, sample_p2 = solve(sample_input)
p1, p2 = solve(input)
print(f"Part 1 answer for sample input: {sample_p1}")
print(f"Part 1 final answer: {p1}")
print(f"Part 2 answer for sample input: {sample_p2}")
print(f"Part 2 final answer: {p2}")