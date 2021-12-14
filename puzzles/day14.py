from .methods import txt_opener
import re
import string


def polymer_insertion(template, ins_rules):
    new_template = ''
    for i in range(len(template)):
        new_template += template[i]
        if template[i:i + 2] in ins_rules.keys():
            new_template += [x for x in ins_rules.values() if x == ins_rules[template[i:i + 2]]][0]

    return new_template


def get_occurrences(template):      # returned example: {'A': 256, 'B': 112, 'C': 49}
    return sorted([{'letter': let, 'total': len(re.findall(let, template))} for let in string.ascii_uppercase if let in template],
                  key=lambda i: i['total'], reverse=True)


def part1(input_file):              # slow calculations are enough
    final_input = txt_opener(input_file, '\n')
    template = final_input[0]
    ins_rules = {row.split(' -> ')[0]: row.split(' -> ')[1] for row in final_input[1:]}

    # get polymer recreated 10 times
    for _ in range(10):
        template = polymer_insertion(template, ins_rules)

    # subtract: most frequent - least frequent character
    letters = get_occurrences(template)
    return letters[0]['total'] - letters[-1]['total']


def part2(input_file):              # fast calculations needed
    final_input = txt_opener(input_file, '\n')
    template = final_input[0]
    ins_rules = {row.split(' -> ')[0]: row.split(' -> ')[1] for row in final_input[1:]}

    # get polymer recreated 10 times
    for _ in range(40):
        template = polymer_insertion(template, ins_rules)

    # subtract: most frequent - least frequent character
    letters = get_occurrences(template)
    return letters[0]['total'] - letters[-1]['total']
