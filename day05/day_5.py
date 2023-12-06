def part_1(filename):
    with open(filename) as file:
        [seeds, seed_to_soil_map, soil_to_fertilizer, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map] = get_almanac(file)
    min_location = float('inf')
    for seed in seeds:
        location = getLocationFromSeed(seed, [seed_to_soil_map, soil_to_fertilizer, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map])
        min_location = min(min_location, location)
    return(min_location)
    
def get_almanac(file):
    seeds = get_seeds(file)
    file.readline()
    file.readline()
    seed_to_soil_map = get_map(file)
    file.readline()
    soil_to_fertilizer = get_map(file)
    file.readline()
    fertilizer_to_water_map = get_map(file)
    file.readline()
    water_to_light_map = get_map(file)
    file.readline()
    light_to_temperature_map = get_map(file)
    file.readline()
    temperature_to_humidity_map = get_map(file)
    file.readline()
    humidity_to_location_map = get_map(file)
    return [seeds, seed_to_soil_map, soil_to_fertilizer, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map]

def get_seeds(file):
    seeds_line = file.readline()
    seeds_number = seeds_line.rstrip('\n').split(': ')[1]
    seeds = seeds_number.split(' ')
    return [int(seed) for seed in seeds]

def get_map(file):
    line = file.readline()
    res = []
    while line and line != '\n':
        line = line.rstrip('\n')
        [destination_range_start, source_range_start, range_length] = line.split(' ')
        res.append([int(destination_range_start), int(source_range_start), int(range_length)])
        line = file.readline()
    return res

def getLocationFromSeed(seed, maps):
    [seed_to_soil_map, soil_to_fertilizer, fertilizer_to_water_map, water_to_light_map, light_to_temperature_map, temperature_to_humidity_map, humidity_to_location_map] = maps
    soil = get_destination_from_source(seed, seed_to_soil_map)
    fertilizer = get_destination_from_source(soil, soil_to_fertilizer)
    water = get_destination_from_source(fertilizer, fertilizer_to_water_map)
    light = get_destination_from_source(water, water_to_light_map)
    temperature = get_destination_from_source(light, light_to_temperature_map)
    humidity = get_destination_from_source(temperature, temperature_to_humidity_map)
    location = get_destination_from_source(humidity, humidity_to_location_map)
    return location
def get_destination_from_source(source, map):
    for [destination_range_start, source_range_start, range_length] in map:
        if source >= source_range_start and source < source_range_start + range_length:
            return destination_range_start + source - source_range_start
    return source
if __name__ == '__main__':
    print(part_1('input.txt'))