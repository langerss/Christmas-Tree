import random

char = [ "@", "#", "*"]
bits = ["0", "1"]
tree_top_one = "*"
tree_top_two = "<|>"
size_tree = 30

def random_bit():
    return random.randint(0,1)

def random_symbol(x):
    return x[random.randint(0,len(x)-1)]

def random_string_gen(length,a_list):
    counter = 1
    string_char = ""
    while counter <= length:
        counter += 1
        string_char += random_symbol(a_list)
    return string_char


def string_of_spaces(length):
    counter = 1
    space_char = ""
    while counter <= length:
        counter += 1
        space_char += " "
    return space_char

def calc_spaces(line_num):
    space_count = size_tree - line_num
    return string_of_spaces(space_count)

def check_prime(test_num):
    test_count = 2
    if test_num == 1:
        return False
    if test_num == 2:
        return True
    while test_count < test_num:
        if test_num % test_count == 0:
            return False
        test_count += 1
    return True

def calc_bits(line_num):
    return line_num * 2 + 1

def build_tree():
    line = 1
    while line <= size_tree:
        num_bits = calc_bits(line)
        tree_line = calc_spaces(line) + random_string_gen(num_bits,bits)
        tree_line = prime_position(tree_line,line)
        print(tree_line)
        line +=1
    return

def build_topper(line):
    if line == 1:
        print(calc_spaces(line-1) + tree_top_one)
    if line == 2:
        print(calc_spaces(line-1) + tree_top_two)
    return

def prime_position(string,line_num):
    char_num = line_num ** 2
    new_string = ""
    for item in string:
        if item not in bits:
            new_string = new_string + item
        else:
            if check_prime(char_num) == True:
                new_string = new_string + random_string_gen(1,char)
            else:
                new_string = new_string + item
            char_num +=1
    return new_string


build_topper(1)
build_topper(2)
build_tree()
