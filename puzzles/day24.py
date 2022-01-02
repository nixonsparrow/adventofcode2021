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


def cmd_inp(a, variables, inputs):
    variables[a] = int(inputs[0])
    inputs = inputs[1:]
    return variables, inputs


def alu(commands, inputs):
    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for command in commands:
        print('COMMAND:', command)
        com = command[0:3]
        print(com)
        if 'inp' == com:
            variables, inputs = cmd_inp(command[4], variables, inputs)

        else:
            a, b = command[3:].split()[0], command[3:].split()[1]
            try:
                b = int(b)
            except ValueError:
                b = variables[b]

            print(a)
            print(b)

            if com == 'add':
                variables[a] = cmd_add(variables[a], b)
            elif com == 'mul':
                variables[a] = cmd_mul(variables[a], b)
            elif com == 'div':
                variables[a] = cmd_div(variables[a], b)
            elif com == 'mod':
                variables[a] = cmd_mod(variables[a], b)
            elif com == 'eql':
                variables[a] = cmd_eql(variables[a], b)
            else:
                raise AttributeError

        print(variables)

    return variables


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return alu(final_input, '1')


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
