from aocd import get_data

input_arr = get_data(day=5, year=2023).splitlines()
    
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

for seed in seeds:    
    # map seed to soil - initialise as seed number in case there is no mapping
    soil_map = seed
    for seed_to_soil in seeds_to_soil:
        for i in range(int(seed_to_soil[2])):
            print(i)
            if seed == int(seed_to_soil[1]) + i:
                soil_map = int(seed_to_soil[0]) + i
                print(soil_map)
                #break
            #print("test")
        

