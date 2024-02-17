from aocd import get_data, submit

def format_data(input_str):
    data = []
    for row in input_str.splitlines():
        winning_numbers, your_numbers = row.split(": ")[1].replace("  ", " ").split(" | ")
        data.append((winning_numbers.strip().split(" "), your_numbers.strip().split(" ")))
    return data

def part_a(input):
    total = 0
    for winning_numbers, your_numbers in input:
        common_numbers = list(set(winning_numbers).intersection(your_numbers))
        total += 2 ** (len(common_numbers)-1) if len(common_numbers) > 0 else 0
    return total

def part_b(input):
    results = [1] * len(input)
    for i, (winning_numbers, your_numbers) in enumerate(input):
        common_numbers = list(set(winning_numbers).intersection(your_numbers))
        for j in range(1, len(common_numbers) + 1):
            results[i+j] += results[i] 
    return sum(results)

if __name__ == "__main__":
    # Testing
    test_string = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

    test_data = format_data(test_string)
    assert part_a(test_data) == 13
    assert part_b(test_data) == 30

    # Solve
    data = format_data(get_data(day=4, year=2023))
    submit(part_a(data), part="a", day=4, year=2023)    
    submit(part_b(data), part="b", day=4, year=2023)