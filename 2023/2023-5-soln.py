from aocd import get_data, submit

def format_data(input_str):
    input_arr = input_str.splitlines()

    seeds = input_arr[0].split(": ")[1].split(" ")

    maps = []
    maps.append(input_arr[input_arr.index("seed-to-soil map:")+1: input_arr.index("soil-to-fertilizer map:")-1])
    maps.append(input_arr[input_arr.index("soil-to-fertilizer map:")+1: input_arr.index("fertilizer-to-water map:")-1])
    maps.append(input_arr[input_arr.index("fertilizer-to-water map:")+1: input_arr.index("water-to-light map:")-1])
    maps.append(input_arr[input_arr.index("water-to-light map:")+1: input_arr.index("light-to-temperature map:")-1])
    maps.append(input_arr[input_arr.index("light-to-temperature map:")+1: input_arr.index("temperature-to-humidity map:")-1])
    maps.append(input_arr[input_arr.index("temperature-to-humidity map:")+1: input_arr.index("humidity-to-location map:")-1])
    maps.append(input_arr[input_arr.index("humidity-to-location map:")+1: len(input_arr)])

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            maps[i][j] = maps[i][j].split(" ")
    
    return seeds, maps

def perform_mapping(map_index, mapping_arr, curr_map):
    for i in range(len(mapping_arr[map_index])):
        if int(mapping_arr[map_index][i][1]) <= int(curr_map) <= (int(mapping_arr[map_index][i][1]) + int(mapping_arr[map_index][i][2])):
            curr_map = int(curr_map) + (int(mapping_arr[map_index][i][0]) - int(mapping_arr[map_index][i][1]))
            break
    return curr_map

def part_a(seeds, maps):
    locations = []
    for seed in seeds:
        current_mapping = seed
        for i in range(len(maps)):
            current_mapping = perform_mapping(i, maps, current_mapping)
        locations.append(current_mapping)
    return(min(locations))

def part_b(seeds, maps):
    locations = []
    for seed in range(int(seeds[0]), int(seeds[0]) + int(seeds[1])):
        current_mapping = seed
        for i in range(len(maps)):
            current_mapping = perform_mapping(i, maps, current_mapping)
        locations.append(current_mapping)
    return(min(locations))
    # haha, does not run. will need to come back later


if __name__ == "__main__":
    # Testing
    test_string = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

    test_seeds, test_maps = format_data(test_string)
    assert part_a(test_seeds, test_maps) == 35
    seeds, maps = format_data(get_data(day=5, year=2023))
    #submit(part_a(seeds, maps), part="a", day=5, year=2023)  
    print(part_b(test_seeds, test_maps))