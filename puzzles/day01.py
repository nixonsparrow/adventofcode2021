from os import path


def sonar_sweep(measures, wide=False):
    if wide:
        return sum([1 for index in range(len(measures)) if index > 2 and measures[index] > measures[index - 3]])
    else:
        return sum([1 for index in range(len(measures)) if index > 0 and measures[index] > measures[index - 1]])


def part1(input_file=''):
    final_input = list(map(int, open(path.dirname(__file__) + input_file)))
    return sonar_sweep(final_input)


def part2(input_file=''):
    final_input = list(map(int, open(path.dirname(__file__) + input_file)))
    return sonar_sweep(final_input, wide=True)
