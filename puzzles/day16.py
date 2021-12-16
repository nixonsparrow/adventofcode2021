from .methods import txt_opener


def get_bin(char):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    if char in letters:
        char = letters.index(char) + 10
    return format(int(char), 'b').zfill(4)


def translate_into_binary(sequence):
    return ''.join([get_bin(char) for char in sequence])


def get_version(binary_code):
    return int(binary_code[0:3], 2)


def get_id(binary_code):
    return int(binary_code[3:6], 2)


def get_length_type_id(binary_code):
    if get_id(binary_code) == 4:
        raise AttributeError
    return int(binary_code[6])


def read_literal_values(value):
    end = True if value[0] == '0' else False
    return value[1:], end


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
