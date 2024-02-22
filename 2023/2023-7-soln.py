from aocd import get_data, submit
from collections import Counter

def format_data(input_str):
    data = []
    for row in input_str.splitlines():
        data.append(row.split(" "))
    return data

def classify_card(card):
    card_rankings = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1
    }
    return card_rankings[card]

def classify_type(hand):
    frequencies = Counter(hand)

    # Five of a kind
    if len(frequencies) == 1:
        return 7
    # Four of a kind OR full house
    elif len(frequencies) == 2:
        for letter in frequencies:
            if frequencies[letter] == 4:
                return 6
        return 5
    # Three of a kind OR two pair
    elif len(frequencies) == 3:
        for letter in frequencies:
            if frequencies[letter] == 3:
                return 4
        return 3
    # One pair
    elif len(frequencies) == 4:
        return 2
    # High card
    elif len(frequencies) == 5:
        return 1

def part_a(input):
    ranks = []
    for i in range(len(input)):
        ranks.append([classify_type(input[i][0])]) # append rank according to type
    
    # Classifying all cards regardless of if it's needed...
    for i in range(len(input)):
        card_index_to_classify = 0
        for j in range(5):
            ranks[i].append(classify_card(input[i][0][card_index_to_classify]))
            card_index_to_classify += 1
        ranks[i].append(i) # appending this at the end to know what the original element index was...

    sorted_hands = sorted(ranks)

    total = 0
    for i, rank in enumerate(sorted_hands):
        total += (i + 1) * int(input[rank[6]][1])
    return total

if __name__ == "__main__":
    # Testing
    test_string = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

    assert part_a(format_data(test_string)) == 6440

    data = format_data(get_data(day=7, year=2023))
    submit(part_a(data), part="a", day=7, year=2023)