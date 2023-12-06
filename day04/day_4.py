def part_1(filename):
    result = 0
    with open(filename) as file:
        for line in file:
            found_numbers = 0
            winning_numbers_set, your_numbers_set = get_winning_numbers_and_your_numbers(line)
            for number in winning_numbers_set:
                if number in your_numbers_set:
                    found_numbers += 1
                    your_numbers_set.remove(number)
            if found_numbers > 0:
                result += 2 ** (found_numbers - 1)

    return result

def get_winning_numbers_and_your_numbers(line):
    line = line.rstrip('\n')
    input = line.split(":")[1].strip()
    winning_numbers, your_numbers = input.split("|")
    winning_numbers, your_numbers = winning_numbers.strip().split(" "), your_numbers.strip().split(" ")
    winning_numbers = filter(lambda x: x.isdigit(), winning_numbers)
    your_numbers = filter(lambda x: x.isdigit(), your_numbers)
    return set(winning_numbers), set(your_numbers)

def part_2(filename):
    winning_numbers = []
    with open(filename) as file:
        for line in file:
            found_numbers = 0
            winning_numbers_set, your_numbers_set = get_winning_numbers_and_your_numbers(line)
            for number in winning_numbers_set:
                if number in your_numbers_set:
                    found_numbers += 1
                    your_numbers_set.remove(number)
            winning_numbers.append(found_numbers)
    nb_of_copies = [1] * len(winning_numbers)
    for i, number in enumerate(winning_numbers):
        for x in range(i + 1, i + 1 + number):
            nb_of_copies[x] += nb_of_copies[i]
    return sum(nb_of_copies)

if __name__ == '__main__':
    print(part_2('input.txt'))