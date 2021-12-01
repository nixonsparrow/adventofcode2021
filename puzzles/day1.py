from os import path


def bunny_jumper(bunny_path, full_course=True):
    # ------------------------------ starting variables
    directions = ['N', 'E', 'S', 'W']
    direction = directions[0]
    position = [0, 0]
    positions_already_visited = []

    for segment in bunny_path:
        steps = int(segment[1:])

        # ------------------------------ turn
        if 'R' in segment:
            try:
                direction = directions[directions.index(direction) + 1]
            except IndexError:
                direction = directions[0]
        elif 'L' in segment:
            try:
                direction = directions[directions.index(direction) - 1]
            except IndexError:
                direction = directions[-1]

        # ------------------------------ move
        # PART 1

        for step in range(steps):
            current_position = tuple(position)

            if not full_course:
                if current_position not in positions_already_visited:
                    positions_already_visited.append(current_position)
                else:
                    break

            if direction == 'N':
                position[0] += 1
            elif direction == 'S':
                position[0] -= 1
            elif direction == 'E':
                position[1] += 1
            elif direction == 'W':
                position[1] -= 1

    # ------------------------------ calculate distance
    distance = sum((abs(position[0]), abs(position[1])))
    return distance


def part1(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).readline().replace(' ', '').split(',')))
    return bunny_jumper(final_input)


def part2(input_file=''):
    final_input = list(map(str, open(path.dirname(__file__) + input_file).readline().replace(' ', '').split(',')))
    return bunny_jumper(final_input, full_course=False)
