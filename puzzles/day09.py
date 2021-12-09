from .methods import txt_opener
import numpy as np


def is_low_point(heightmap, target_x, target_y):
    target = heightmap[target_x][target_y]
    surroundings = []

    for x, y in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        try:
            if target_x + x < 0 or target_y + y < 0:
                continue
            surroundings.append(heightmap[target_x + x][target_y + y])
        except IndexError:
            pass

    # return True only if all 2-4 surroundings are higher than target spot
    return True if all([True if target < neighbour else False for neighbour in surroundings]) else False


def get_low_points(heightmap):
    ys, xs = len(heightmap[0]), len(heightmap)
    return {(x, y): heightmap[x][y] for x in range(xs) for y in range(ys) if is_low_point(heightmap, x, y)}


def get_basin(coordinates, heightmap):
    x, y = coordinates[0], coordinates[1]
    old_basin, new_basin = {}, [(x, y)]

    while old_basin != new_basin:       # check for all 4 neighbour squares coordinates
        old_basin = new_basin           # for every not yet checked square
        for x, y in new_basin:
            for xi, yi in ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)):
                try:
                    if (xi, yi) not in new_basin and heightmap[xi][yi] != 9 and \
                            all([xi >= 0, yi >= 0]):
                        new_basin.append((xi, yi))
                except IndexError:      # ignore if coordinates are beyond
                    pass

    return new_basin


def multiple_3_biggest_basins(basin_sizes):
    return np.prod(sorted(basin_sizes, reverse=True)[0:3])


def part1(input_file):
    final_input = txt_opener(input_file, '\n', force_str=True)
    heightmap = [[int(char) for char in row]for row in final_input]
    low_points = list(get_low_points(heightmap).values())
    return sum(low_points, len(low_points))


def part2(input_file):
    final_input = txt_opener(input_file, '\n', force_str=True)
    heightmap = [[int(char) for char in row]for row in final_input]
    low_points = get_low_points(heightmap)
    basin_sizes = [len(get_basin(coordinates, heightmap)) for coordinates in low_points]
    return multiple_3_biggest_basins(basin_sizes)
            