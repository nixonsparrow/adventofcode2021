from .methods import txt_opener


def cmd_add(a, b):
    return sum((a, b))


def cmd_mul(a, b):
    return a * b


def cmd_div(a, b):
    return a // b


def cmd_mod(a, b):
    return a % b


def cmd_eql(a, b):
    return 1 if a == b else 0


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
