from aocd import get_data, submit

def format_data_a(input_str):
    time_arr = " ".join(input_str.splitlines()[0].replace("Time:", "").split()).split(" ")
    distance_arr = " ".join(input_str.splitlines()[1].replace("Distance:", "").split()).split(" ")
    return time_arr, distance_arr

def format_data_b(input_str):
    time = input_str.splitlines()[0].replace("Time:", "").replace(" ", "")
    distance = input_str.splitlines()[1].replace("Distance:", "").replace(" ", "")
    return time, distance

def part_a(times, distances):
    product = 1
    for i, race_time in enumerate(times):
        num_times_beaten = 0
        for j in range(int(race_time) + 1):
            race_distance = j * (int(race_time) - j)
            if race_distance > int(distances[i]):
                num_times_beaten += 1
        product = product * num_times_beaten
    return product

def part_b(time, distance):
        num_times_beaten = 0
        for j in range(int(time) + 1):
            race_distance = j * (int(time) - j)
            if race_distance > int(distance):
                num_times_beaten += 1
        return num_times_beaten

if __name__ == "__main__":
    # Testing
    test_string = '''Time:      7  15   30
Distance:  9  40  200'''

    test_time_a, test_distance_b = format_data_a(test_string)
    assert part_a(test_time_a, test_distance_b) == 288

    test_time_b, test_distance_b = format_data_b(test_string)
    assert part_b(test_time_b, test_distance_b) == 71503

    time_a, distance_a = format_data_a(get_data(day=6, year=2023))
    submit(part_a(time_a, distance_a), part="a", day=6, year=2023)

    time_b, distance_b = format_data_b(get_data(day=6, year=2023))
    submit(part_b(time_b, distance_b), part="b", day=6, year=2023)