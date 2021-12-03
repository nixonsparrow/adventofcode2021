from os import path
from .methods import txt_opener


def calculate_power_consumption(gamma_rate, epsilon_rate):
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_life_support_rating(oxygen_generator_rating, co2_scrubber_rating):
    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


def read_gamma_rate(diagnostic_report, epsilon=False):
    arr = [[int(word[i]) for word in diagnostic_report] for i in range(len(diagnostic_report[0]))]
    gamma_rate = ''.join(['1' if sum(arr[i]) / len(arr[i]) > 0.5 else '0' for i in range(len(arr))])
    if epsilon:
        return ''.join(['0' if gamma_rate[i] == '1' else '1' for i in range(len(gamma_rate))])
    return gamma_rate


def check_real_bit(arr, position, co2=False):
    new_arr = [[int(word[i]) for word in arr] for i in range(len(arr[0]))]
    if co2:
        return '0' if sum(new_arr[position]) / len(new_arr[position]) >= 0.5 else '1'
    return '1' if sum(new_arr[position]) / len(new_arr[position]) >= 0.5 else '0'


def remove_wrong_numbers(arr, position, co2=False):
    bit = check_real_bit(arr, position, co2=co2)
    return [nr for nr in arr if nr[position] == bit]


def read_oxygen_generator_rating(diagnostic_report, co2=False):
    i, max_i = 0, len(diagnostic_report[0])
    while len(diagnostic_report) > 1:
        diagnostic_report = remove_wrong_numbers(diagnostic_report, i, co2=co2)
        i += 1 if i < max_i else - max_i

    return diagnostic_report[0]


def part1(input_file=''):
    final_input = txt_opener(input_file, '\n', force_str=True)
    gamma_rate = read_gamma_rate(final_input)
    epsilon_rate = read_gamma_rate(final_input, epsilon=True)
    return calculate_power_consumption(gamma_rate, epsilon_rate)


def part2(input_file=''):
    final_input = txt_opener(input_file, '\n', force_str=True)
    oxygen_generator_rating = read_oxygen_generator_rating(final_input)
    co2_scrubber_rating = read_oxygen_generator_rating(final_input, co2=True)
    return calculate_life_support_rating(oxygen_generator_rating, co2_scrubber_rating)
