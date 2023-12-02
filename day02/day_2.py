import re
from functools import reduce

limits_per_color = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def part_1(filename):
    total = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip('\n')
            game_string, game_input = line.split(":")
            game_number = int(game_string.split(" ")[-1])
            throws = re.split(",|;", game_input)
            throws = [x.lstrip(" ") for x in throws]
            throws_are_in_limit = list(map(lambda throw: is_throw_respecting_limits(throw), throws))
            if (all(throw_is_in_limit == True for throw_is_in_limit in throws_are_in_limit)):
                total += game_number
    return total

def is_throw_respecting_limits(throw):
    cubes_number, cubes_color = throw.split(" ")
    return int(cubes_number) <= limits_per_color[cubes_color]

###############################################################

def part_2(filename):
    total = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip('\n')
            game_string, game_input = line.split(":")
            game_number = int(game_string.split(" ")[-1])
            throws = re.split(",|;", game_input)
            throws = [x.lstrip(" ") for x in throws]
            lowest_number_of_cubes_per_color = get_lowest_number_of_cubes_per_color(throws)
            total += get_power_of_cube_set(lowest_number_of_cubes_per_color)
    return total

def get_lowest_number_of_cubes_per_color(throws):
    dic = {}
    for throw in throws:
        cubes_number, cubes_color = throw.split(" ")
        if cubes_color in dic:
            dic[cubes_color] = max(int(cubes_number), dic[cubes_color])
        else:
            dic[cubes_color] = int(cubes_number)
    return dic

def get_power_of_cube_set(lowest_number_of_cubes_per_color):
    number_of_cubes = [value for key, value in lowest_number_of_cubes_per_color.items()]
    return reduce(lambda acc, curr: acc * curr, number_of_cubes)

if __name__ == '__main__':
    part_1()
