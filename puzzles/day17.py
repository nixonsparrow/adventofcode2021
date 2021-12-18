from .methods import txt_opener


def read_target_area(_input):
    coordinates = _input.split(': ')[1].split(', ')
    target_area = []
    for coord in coordinates:
        values = coord[2:].split('..')
        target_area.append((int(values[0]), int(values[1])))

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
    last = trajectory[-1]
    while (x + last[0]) < target[0][1] + 1 and (y + last[1]) > target[1][0] - 1:
        last = trajectory[-1]
        trajectory.append((x + last[0], y + last[1]))
        if check_if_probe_hits_target(trajectory[-1][0], trajectory[-1][1], target): return trajectory
        x += 1 if x < 0 else - 1 if x > 0 else 0
        y -= 1

    return []


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    target = read_target_area(final_input)
    xs = get_xs_that_may_hit(target)
    highest_y = 0
    for x in xs:
        for y in range(100):
            trajectory = calculate_trajectory(x, y, target)
            temp_y = get_highest_position(trajectory) if trajectory else 0
            if temp_y > highest_y:
                highest_y = temp_y
    return highest_y


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    target = read_target_area(final_input)
    velocities = []
    for x in range(target[0][1] + 1):
        for y in range(target[1][0] - 1, 100):
            trajectory = calculate_trajectory(x, y, target)
            for coord in trajectory:
                if check_if_probe_hits_target(coord[0], coord[1], target):
                    velocities.append((x, y))
    return len(velocities)
