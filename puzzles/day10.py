from .methods import txt_opener


def autocomplete_tool(sequence):
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    score = 0
    for value in [points[br] for br in sequence[::-1]]:
        score = 5 * score + value
    return score


def search_for_bracket_closures(sequence):
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    brackets = {'[': ']', '<': '>', '{': '}', '(': ')'}
    opened_brackets = []

    for i in range(len(sequence)):

        # if bracket opens
        if sequence[i] in '{[(<':
            opened_brackets.append(sequence[i])

        else:   # if wrong closing bracket return points of that bracket
            for k, v in brackets.items():
                if v == sequence[i] and opened_brackets[-1] != k:
                    # return broken string
                    return points[sequence[i]]

            # if bracket is closed properly
            opened_brackets.pop(-1)

    # return unclosed bracket in string
    return ''.join([br for br in opened_brackets])


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return sum([search_for_bracket_closures(sequence) for sequence in final_input if type(search_for_bracket_closures(sequence)) == int])


def part2(input_file):
    final_input = txt_opener(input_file, '\n')

    # get all sequences without wrong closing bracket
    sequences = [search_for_bracket_closures(sequence) for sequence in final_input if type(search_for_bracket_closures(sequence)) != int]

    sorted_results = sorted([autocomplete_tool(seq) for seq in sequences])
    return sorted_results[len(sorted_results)//2]
