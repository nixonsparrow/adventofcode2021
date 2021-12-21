import re
from .methods import txt_opener


def sum_nests(nest_a, nest_b):
    return f'[{nest_a},{nest_b}]'


def explode_index(nest):
    ex_index = 0
    opened_brackets = 0

    for i in range(len(nest)):
        if nest[i] == '[':
            opened_brackets += 1
            if opened_brackets == 5:
                return ex_index
        elif nest[i] == ']':
            opened_brackets -= 1

        ex_index += 1
    return False


def explode_nest(nest):
    i = explode_index(nest)
    if not i: return False

    nrs = re.findall(r'\d+', nest[i:i + 5])
    if len(nrs) < 2: nrs = re.findall(r'\d+', nest[i:i + 6])
    # l_db = True if len(nrs[0]) > 1 else False
    # r_db = True if len(nrs[1]) > 1 else False
    print(i, nrs)
    left_nr, right_nr = None, None

    l_i = i
    while l_i > 0:
        try:
            left_nr = int(nest[l_i])
            break
        except ValueError: pass
        l_i -= 1

    r_i = i + 5
    while r_i < len(nest) - 1:
        try:
            right_nr = int(nest[r_i])
            break
        except ValueError: pass
        r_i += 1

    print('1:', nest)
    l_double_digit = None
    if left_nr is not None:
        # l_i_after = l_i + 2 if len(nrs[0]) > 1 else l_i + 1
        try:
            l_double_digit = int(nest[l_i:l_i + 2])
            nest = f'{nest[:l_i]}{str(int(nrs[0]) + l_double_digit)}{nest[l_i + 2:]}'
        except ValueError:
            nest = f'{nest[:l_i]}{str(int(nrs[0]) + left_nr)}{nest[l_i + 1:]}'
    print('2:', nest, r_i)
    if right_nr is not None:
        # r_i_after = r_i + 2 if len(nrs[0]) > 1 else r_i + 1
        try:
            r_double_digit = int(nest[r_i:r_i + 2])
            nest = f'{nest[:r_i + (1 if l_double_digit else 0)]}{str(int(nrs[1]) + r_double_digit)}{nest[r_i + 2:]}'
        except ValueError:
            nest = f'{nest[:r_i + (1 if l_double_digit else 0)]}{str(int(nrs[1]) + right_nr)}{nest[r_i + 1:]}'
    print('3:', nest)

    x = 5
    for nr in nrs:
        x += 1 if len(nr) > 1 else 0

    nest = nest[:i] + nest[i + x:]
    print('4:', nest)

    while '[]' in nest: nest = nest.replace('[]', '0')
    nest = nest.replace(',]', ',0]')
    nest = nest.replace('[,', '[0,')
    print('5:', nest)
    # while '[]' in nest:
    #     nest.replace('[]', '')
    # while ',,' in nest:
    #     nest.replace(',,', ',')

    return nest


def split_index(nest):
    for nr in re.findall(r'\d\d', nest):
        return nest.index(nr)

    return False


def split_nest(nest):
    if explode_index(nest):
        return False
    i = split_index(nest)

    nr = int(nest[i:i + 2])
    splitted = nest[:i] + f'[{nr // 2 if nr % 2 == 0 else nr // 2 + 1},{nr//2}]' + nest[i + 2:]
    print('Splitted:', splitted)
    print()
    return splitted


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    nest = final_input[0]
    final_input = final_input[1:]
    for row in final_input:
        print('pre_row  ', nest)
        nest = sum_nests(nest, row)
        print('after_row', nest)
        while explode_index(nest) or split_index(nest):
            print('found split:', split_index(nest))
            while split_index(nest):
                nest = split_nest(nest) if split_index(nest) else nest
                continue
            while explode_index(nest):
                print('pre explode   ', nest)
                nest = explode_nest(nest) if explode_index(nest) else nest
                print('after explode ', nest)
                print()
            print()
    return nest


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
