from itertools import accumulate
from .methods import txt_opener


def read_target_area(_input):
    coordinates = _input.split(': ')[1].split(', ')
    target_area = []
    for coord in coordinates:
        values = coord[2:].split('..')
        target_area.append((int(min(values)), int(max(values))))

    return tuple(target_area)


def check_if_probe_hits_target(x, y, target_area):
    x_range, y_range = range(target_area[0][0], target_area[0][1] + 1), range(target_area[1][0], target_area[1][1] + 1)
    return True if x in x_range and y in y_range else False


def get_highest_position(trajectory):
    return max(y for x, y in trajectory)


def get_xs_that_may_hit(target_area):
    xs = [0]
    x = 0
    while xs[-1] < target_area[0][1]:
        x += 1
        xs.append(x + xs[-1])

    return [xs.index(x) for x in xs if target_area[0][0] <= x <= target_area[0][1]]




def calculate_trajectory(x, y, target):
    trajectory = [(0, 0)]
    print('1', trajectory)
    while y > target[1][0] - 1 and x < target[0][1] + 1:
        print('2', trajectory)
        last = trajectory[-1]
        trajectory.append((x + last[0], y + last[1]))
        if check_if_probe_hits_target(trajectory[-1][0], trajectory[-1][1], target): break
        x += 1 if x < 0 else - 1
        y -= 1

    return trajectory


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    target = read_target_area(final_input)

    return final_input


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
