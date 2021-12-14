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


def update_polymer_dictionary(polymers, ins_rules):
    new_polymers = {k: 0 for k in polymers}
    for pair, single in ins_rules.items():
        new_polymers[pair[0] + single] += polymers[pair]
        new_polymers[single + pair[1]] += polymers[pair]

    return new_polymers


def get_letter_occurrences(letters, polymers, last_letter):
    for pair, value in polymers.items():
        letters[pair[0]] += value
    letters[last_letter] += 1

    return letters


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

    # replace the template with a dictionary of polymer pairs
    all_possible_letters = []
    [all_possible_letters.append(letter) for letter in list(template) + list(ins_rules.values()) if letter not in all_possible_letters]

    # create dictionary with pairs then find and count all pairs in the template
    pairs = {letter_a + letter_b: 0 for letter_a in all_possible_letters for letter_b in all_possible_letters}
    polymers = {pair: len(re.findall(pair, template)) for pair in pairs.keys()}

    # get polymer recreated 40 times
    for _ in range(40):
        polymers = update_polymer_dictionary(polymers, ins_rules)

    letters = {letter: 0 for letter in all_possible_letters}
    letters = get_letter_occurrences(letters, polymers, template[-1])

    return max(letters.values()) - min(letters.values())
