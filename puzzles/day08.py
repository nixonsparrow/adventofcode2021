from .methods import txt_opener


def get_same_bars(a_bars, b_bars):
    return sum([1 for x in a_bars for y in b_bars if x == y])


def get_digit(sequence, dictionary):
    for digit, v in dictionary.items():
        if get_same_bars(v, sequence) == len(v) and get_same_bars(v, sequence) == len(sequence):
            return digit


def dictionary_writer(x_digits):
    digits = {str(digit): '' for digit in range(10)}
    while '' in digits.values():
        for x_digit in x_digits.split():
            if x_digit not in digits.values():      # exclude digits already known
                if len(x_digit) == 2:               # check for obvious digit codes 1/4/7/8
                    digits['1'] = x_digit
                elif len(x_digit) == 4:
                    digits['4'] = x_digit
                elif len(x_digit) == 3:
                    digits['7'] = x_digit
                elif len(x_digit) == 7:
                    digits['8'] = x_digit
                else:
                    if len(x_digit) == 5:               # search for 2/3/5 based on similar bars number
                        if get_same_bars(x_digit, digits['9']) == 4:
                            digits['2'] = x_digit
                        else:
                            if get_same_bars(x_digit, digits['7']) == 3:
                                digits['3'] = x_digit
                            else:
                                digits['5'] = x_digit
                    else:                               # search for 6/9/0 based on similar bars number
                        if get_same_bars(x_digit, digits['7']) == 2:
                            digits['6'] = x_digit
                        else:
                            if get_same_bars(x_digit, digits['4']) == 4:
                                digits['9'] = x_digit
                            else:
                                digits['0'] = x_digit
    return digits


def get_four_digit_code(x_digits, x_code):
    # create dictionary based on given data
    digits = dictionary_writer(x_digits)

    code = ''
    for x in x_code.split():
        code += get_digit(x, digits)

    return code


def part1(input_file):
    final_input = txt_opener(input_file, '\n')

    # exercise is too simple to spread it
    # just get total count of sequences with 2, 3, 4 or 7 chars on the right side of input
    return sum([sum([1 if len(digit) in [2, 3, 4, 7] else 0 for digit in row.split(' | ')[1].split()]) for row in final_input])


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    four_digit_codes = []

    # collect all codes in dictionary
    for row in final_input:
        digits, code = row.split(' | ')
        four_digit_codes.append(get_four_digit_code(digits, code))

    # sum all codes as integers
    return sum([int(code) for code in four_digit_codes])
            