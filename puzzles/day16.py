from .methods import txt_opener


def get_bin(char):
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    if char in letters:
        char = letters.index(char) + 10
    return format(int(char), 'b').zfill(4)


def translate_into_binary(sequence):
    return ''.join([get_bin(char) for char in sequence])


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
