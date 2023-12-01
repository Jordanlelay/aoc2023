def part_1(filename):
    with open(filename) as file:
        total = 0
        for line in file:
            left = get_first_digit(line)
            right = get_last_digit(line)
            string_combination = str(line[left]) + str(line[right])
            int_combination = int(string_combination)
            total += int_combination
    return total

def get_first_digit(line):
    left = 0
    while not str.isdigit(line[left]):
        if left >= len(line):
            left = 0
            break
        left += 1
    return left

def get_last_digit(line):
    right = get_right_index(line)
    while not str.isdigit(line[right]):
        if right < 0:
            right = 0
            break
        right -= 1
    return right

def get_right_index(line):
    right = len(line) - 1
    if line[right] == '\n':
        right -= 1
    return right

##############################################################################################################

def part_2(filename):
    total = 0
    with open(filename) as file:
        for line in file:
            first = get_first_digit_or_word(line)
            last = get_last_digit_or_word(line)
            string_combination = get_string_combination(first, last)            
            total += int(string_combination)
    return total

def get_first_digit_or_word(line):
    for i in range(0, len(line) - 1):
        word = check_if_word_in_trie(i, line)
        if word:
            return word

def check_if_word_in_trie(index, line):
    if index >= len(line) or index < 0:
        return False
    current_dict = trie_in_order
    word = ''
    while (line[index] in current_dict):
        word += line[index]
        current_dict = current_dict[line[index]]
        index += 1
        if '_end_' in current_dict:
            return word
    if str.isdigit(line[index]):
        return line[index]

def get_last_digit_or_word(line):
    for i in range(len(line) - 1, -1, -1):
        word = check_if_word_in_trie_reversed(i, line)
        if word:
            return word[::-1]
    
def check_if_word_in_trie_reversed(index, line):
    if index >= len(line) or index < 0:
        return False
    current_dict = trie_reversed
    word = ''
    while (line[index] in current_dict):
        word += line[index]
        current_dict = current_dict[line[index]]
        index -= 1
        if '_end_' in current_dict:
            return word
    if str.isdigit(line[index]):
        return line[index]

def get_string_combination(first, last):
    string_combination = ''
    if str.isdigit(first):
        string_combination += str(first)
    else:
        string_combination += WORDS_TO_DIGIT[first]
    if str.isdigit(last):
        string_combination += str(last)
    else:
        string_combination += WORDS_TO_DIGIT[last]
    return string_combination

def make_trie(words_list):
    root = dict()
    for word in words_list:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict = current_dict.setdefault('_end_', '_end_')
    return root

LIST_OF_DIGITS_IN_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
WORDS_TO_DIGIT = {word: str(i) for i, word in enumerate(LIST_OF_DIGITS_IN_WORDS)}

trie_in_order = make_trie(LIST_OF_DIGITS_IN_WORDS)
trie_reversed = make_trie([word[::-1] for word in LIST_OF_DIGITS_IN_WORDS])

if __name__ == '__main__':
    part_2()
