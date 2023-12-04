def part_1(filename):
    matrix = get_matrix(filename)
    all_adjacent_numbers = []
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            if is_a_symbol(matrix[line][column]):
                adjacent_numbers = get_adjacent_numbers(matrix, line, column)
                all_adjacent_numbers += adjacent_numbers
    return sum(all_adjacent_numbers)

def get_matrix(filename):
    matrix = []
    with open(filename) as file:
        for line in file:
            matrix.append(list(line.rstrip('\n')))
    return matrix

def is_a_symbol(char):
    return not char.isdigit() and char != "."

def get_adjacent_numbers(matrix, line, column):
    adjacent_numbers = []
    if is_top_left_candidate(line, column):
        top_left = get_number(matrix, line - 1, column - 1)
        if top_left:
            adjacent_numbers.append(int(top_left))
            remove_number(matrix, line - 1, column - 1)

    if is_top_candidate(line):
        top = get_number(matrix, line - 1, column)
        if top:
            adjacent_numbers.append(int(top))
            remove_number(matrix, line - 1, column)

    if is_top_right_candidate(len(matrix[line]), line, column):
        top_right = get_number(matrix, line - 1, column + 1)
        if top_right:
            adjacent_numbers.append(int(top_right))
            remove_number(matrix, line - 1, column + 1)

    if is_left_candidate(column):
        left = get_number(matrix, line, column - 1)
        if left:
            adjacent_numbers.append(int(left))
            remove_number(matrix, line, column - 1)
    
    if is_right_candidate(len(matrix[line]), column):
        right = get_number(matrix, line, column + 1)
        if right:
            adjacent_numbers.append(int(right))
            remove_number(matrix, line, column + 1)

    if is_bottom_left_candidate(len(matrix), line, column):
        bottom_left = get_number(matrix, line + 1, column - 1)
        if bottom_left:
            adjacent_numbers.append(int(bottom_left))
            remove_number(matrix, line + 1, column - 1)

    if is_bottom_candidate(len(matrix), line):
        bottom = get_number(matrix, line + 1, column)
        if bottom:
            adjacent_numbers.append(int(bottom))
            remove_number(matrix, line + 1, column)

    if is_bottom_right_candidate(len(matrix), len(matrix[line]), line, column):
        bottom_right = get_number(matrix, line + 1, column + 1)
        if bottom_right:
            adjacent_numbers.append(int(bottom_right))
            remove_number(matrix, line + 1, column + 1)

    return adjacent_numbers

def is_top_left_candidate(line, column):
    return line > 0 and column > 0

def get_number(matrix, line, column):
    if not matrix[line][column].isdigit():
        return False
    
    result = matrix[line][column]
    left = column - 1 
    right = column + 1

    while left >= 0 and matrix[line][left].isdigit():
        result = matrix[line][left] + result
        left -= 1
    while right < len(matrix[line]) and matrix[line][right].isdigit():
        result += matrix[line][right]
        right += 1
    
    return result

def remove_number(matrix, line, column):
    left = column - 1
    right = column + 1
    while left >= 0 and matrix[line][left].isdigit():
        matrix[line][left] = "."
        left -= 1
    while right < len(matrix[line]) and matrix[line][right].isdigit():
        matrix[line][right] = "."
        right += 1

def is_top_candidate(line):
    return line > 0

def is_top_right_candidate(line_length, line, column):
    return line > 0 and column < line_length - 1

def is_left_candidate(column):
    return column > 0

def is_right_candidate(line_length, column):
    return column < line_length - 1

def is_bottom_left_candidate(matrix_length, line, column):
    return line < matrix_length - 1 and column > 0

def is_bottom_candidate(matrix_length, line):
    return line < matrix_length - 1

def is_bottom_right_candidate(matrix_length, line_length, line, column):
    return line < matrix_length - 1 and column < line_length - 1

#######################################################

def part_2(filename):
    matrix = get_matrix(filename)
    all_gear_ratios = 0
    for line in range(len(matrix)):
        for column in range(len(matrix[line])):
            if is_a_gear_symbol(matrix[line][column]):
                adjacent_numbers = get_adjacent_numbers(matrix, line, column)
                if (len(adjacent_numbers) == 2):
                    all_gear_ratios += adjacent_numbers[0] * adjacent_numbers[1]
    return all_gear_ratios

def is_a_gear_symbol(char):
    return char == "*"

if __name__ == '__main__':
    print(part_2('input.txt'))