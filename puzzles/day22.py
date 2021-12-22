from .methods import txt_opener


def prepare_commands(the_input):
    commands = []
    for row in the_input:
        turn_on = True if row[0:2] == 'on' else False
        coord = row.split('=')
        x = tuple([int(ix) for ix in coord[1][:-2].split('..')])
        y = tuple([int(iy) for iy in coord[2][:-2].split('..')])
        z = tuple([int(iz) for iz in coord[3].split('..')])
        commands.append({'on': turn_on, 'x': x, 'y': y, 'z': z})
    return commands


def form_cuboid(commands):
    cuboid = {}

    for com in commands:
        if -50 <= com['x'][0] and com['x'][1] <= 50 and\
           -50 <= com['y'][0] and com['y'][1] <= 50 and\
           -50 <= com['z'][0] and com['z'][1] <= 50:

            for x in range(com['x'][0], com['x'][1] + 1):
                for y in range(com['y'][0], com['y'][1] + 1):
                    for z in range(com['z'][0], com['z'][1] + 1):
                        cuboid[(x, y, z)] = com['on']
    return cuboid


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    cuboid = form_cuboid(prepare_commands(final_input))

    return sum([1 for x in cuboid.values() if x])


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    cuboid = form_cuboid(prepare_commands(final_input))

    return sum([1 for x in cuboid.values() if x])
