
if __name__ == '__main__':
    for day in range(5, 26):
        nr = day if len(str(day)) > 1 else f'0{day}'
        with open(f'day{nr}.py', 'w+') as x:
            x.write(r'''from .methods import txt_opener            


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
            ''')
