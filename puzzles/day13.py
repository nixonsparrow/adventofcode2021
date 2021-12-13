from .methods import txt_opener


def create_transparent_paper(some_input):
    paper = []
    instructions = []
    for row in some_input:
        if row[0:4] == 'fold':
            line, nr = row.split('=')
            instructions.append({'axis': line[-1], 'value': int(nr)})

        elif not row == '':
            coordinates = tuple(map(int, row.split(',')))
            paper.append(coordinates)

    return sorted(paper), instructions


def fold_paper(paper, instruction):
    if instruction['axis'] == 'x':
        new_paper = [dot for dot in paper if dot[0] < instruction['value']]
        for dot in paper:
            if dot[0] > instruction['value']:
                new_dot = (instruction['value'] - abs(dot[0] - instruction['value']), dot[1])
                if new_dot not in new_paper:
                    new_paper.append(new_dot)

    else:
        new_paper = [dot for dot in paper if dot[1] < instruction['value']]
        for dot in paper:
            if dot[1] > instruction['value']:
                new_dot = (dot[0], instruction['value'] - abs(dot[1] - instruction['value']))
                if new_dot not in new_paper:
                    new_paper.append(new_dot)

    return sorted(new_paper)


def paper_folder(paper, instructions):
    for instruction in instructions:
        paper = fold_paper(paper, instruction)

    return paper


def print_paper(paper, print_it=False):
    x = max(dot[0] for dot in paper) + 1
    y = max(dot[1] for dot in paper) + 1
    to_print = ''
    for col in range(y):
        for row in range(x):
            to_print += '#' if (row, col) in paper else '.'
        to_print += '\n'

    if print_it:
        print(to_print)
    return to_print


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    paper, instructions = create_transparent_paper(final_input)
    paper = paper_folder(paper, instructions[:1])
    return len(paper)


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    paper, instructions = create_transparent_paper(final_input)
    paper = paper_folder(paper, instructions)
    print_paper(paper)
    return paper
