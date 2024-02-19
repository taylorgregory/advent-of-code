from aocd import get_data, submit

def part_a(input):
    input_arr = input.splitlines()

    seeds = input_arr[0].split(": ")[1].split(" ")

    seeds_to_soil = input_arr[input_arr.index("seed-to-soil map:")+1: input_arr.index("soil-to-fertilizer map:")-1]
    for i in range(len(seeds_to_soil)):
        seeds_to_soil[i] = seeds_to_soil[i].split(" ")

    soil_to_fertilizer = input_arr[input_arr.index("soil-to-fertilizer map:")+1: input_arr.index("fertilizer-to-water map:")-1]
    for i in range(len(soil_to_fertilizer)):
        soil_to_fertilizer[i] = soil_to_fertilizer[i].split(" ")

    fertilizer_to_water = input_arr[input_arr.index("fertilizer-to-water map:")+1: input_arr.index("water-to-light map:")-1]
    for i in range(len(fertilizer_to_water)):
        fertilizer_to_water[i] = fertilizer_to_water[i].split(" ")

    water_to_light = input_arr[input_arr.index("water-to-light map:")+1: input_arr.index("light-to-temperature map:")-1]
    for i in range(len(water_to_light)):
        water_to_light[i] = water_to_light[i].split(" ")

    light_to_temperature = input_arr[input_arr.index("light-to-temperature map:")+1: input_arr.index("temperature-to-humidity map:")-1]
    for i in range(len(light_to_temperature)):
        light_to_temperature[i] = light_to_temperature[i].split(" ")

    temperature_to_humidity = input_arr[input_arr.index("temperature-to-humidity map:")+1: input_arr.index("humidity-to-location map:")-1]
    for i in range(len(temperature_to_humidity)):
        temperature_to_humidity[i] = temperature_to_humidity[i].split(" ")

    humidity_to_location = input_arr[input_arr.index("humidity-to-location map:")+1: len(input_arr)]
    for i in range(len(humidity_to_location)):
        humidity_to_location[i] = humidity_to_location[i].split(" ")
    
    locations = []
    for seed in seeds:
        # map seed to soil - initialise as seed number in case there is no mapping
        soil_map = seed
        for soil in seeds_to_soil:
            if int(soil[1]) <= int(seed) <= (int(soil[1]) + int(soil[2])):
                soil_map = int(seed) + (int(soil[0]) - int(soil[1]))
        
        fertilizer_map = soil_map
        for fertilizer in soil_to_fertilizer:
            if int(fertilizer[1]) <= int(soil_map) <= (int(fertilizer[1]) + int(fertilizer[2])):
                fertilizer_map = int(soil_map) + (int(fertilizer[0]) - int(fertilizer[1]))

        water_map = fertilizer_map
        for water in fertilizer_to_water:
            if int(water[1]) <= int(fertilizer_map) <= (int(water[1]) + int(water[2])):
                water_map = int(fertilizer_map) + (int(water[0]) - int(water[1]))

        light_map = water_map
        for light in water_to_light:
            if int(light[1]) <= int(water_map) <= (int(light[1]) + int(light[2])):
                light_map = int(water_map) + (int(light[0]) - int(light[1]))

        temp_map = light_map
        for temp in light_to_temperature:
            if int(temp[1]) <= int(light_map) <= (int(temp[1]) + int(temp[2])):
                temp_map = int(light_map) + (int(temp[0]) - int(temp[1]))

        humidity_map = temp_map
        for humidity in temperature_to_humidity:
            if int(humidity[1]) <= int(temp_map) <= (int(humidity[1]) + int(humidity[2])):
                humidity_map = int(temp_map) + (int(humidity[0]) - int(humidity[1]))

        location_map = humidity_map
        for location in humidity_to_location:
            if int(location[1]) <= int(humidity_map) <= (int(location[1]) + int(location[2])):
                location_map = int(humidity_map) + (int(location[0]) - int(location[1]))
        locations.append(location_map)
    return(min(locations))

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

    #part_a(test_string)
    data = get_data(day=5, year=2023)
    submit(part_a(data), part="a", day=5, year=2023)  