from .methods import txt_opener


def dumbos_flash_festival(grid, dumbos_that_flashed):
    for dumbo in dumbos_that_flashed:
        y, x = dumbo
        grid[y][x] = 0
    return grid, len(dumbos_that_flashed)


def search_for_flashes(grid):
    dumbos_that_flashed = []
    old_flashes = None      # later it becomes a list, but None value is needed for first comparison

    # multiple searches needed because flash can increase previous dumbo's power to more than 9
    while old_flashes != dumbos_that_flashed:
        old_flashes = dumbos_that_flashed.copy()
        y = 0
        for octopus_row in grid:
            x = 0
            for dumbo in octopus_row:
                # DUMBO FLASH ENERGY SPREAD
                if dumbo > 9 and (y, x) not in dumbos_that_flashed:
                    dumbos_that_flashed.append((y, x))
                    for a in [-1, 0, 1]:
                        for b in [-1, 0, 1]:
                            try:
                                if y + a >= 0 and x + b >= 0:   # ignore if [y+a][x+b] out of grid
                                    grid[y + a][x + b] += 1
                            except IndexError:
                                pass
                x += 1
            y += 1

    return grid, dumbos_that_flashed


def go_one_step(grid):
    grid = [[nr + 1 for nr in row] for row in grid]

    grid, dumbos_that_flashed = search_for_flashes(grid)

    return dumbos_flash_festival(grid, dumbos_that_flashed)


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    grid = [[int(nr) for nr in str(row)] for row in final_input]

    flashes = 0
    for _ in range(100):
        grid, temp_flashes = go_one_step(grid)
        flashes += temp_flashes
    return flashes


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    grid = [[int(nr) for nr in str(row)] for row in final_input]
    step = 0
    while grid != [[0 for _ in range(10)] for __ in range(10)]:
        grid = go_one_step(grid)[0]
        step += 1
    return step
            