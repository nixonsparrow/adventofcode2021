from .methods import txt_opener
from itertools import accumulate


def sum_total_fuel_needed(positions, target, that_simple=True):
    if not that_simple:
        fuel = 0
        for pos in positions:
            i = 1
            for r in range(abs(pos - target)):
                fuel += i
                i += 1
        return fuel
    return sum([abs(pos - target) for pos in positions])


# calculate least possible fuel needed
def fuel_calculator(positions, simple=True):
    # get rounded average position
    avg = len(positions)//2
    least_fuel = sum_total_fuel_needed(positions, avg, simple)

    # loop check if +1 position is better until it's not
    while avg <= len(positions):
        if sum_total_fuel_needed(positions, avg + 1) < least_fuel:
            avg += 1
            least_fuel = sum_total_fuel_needed(positions, avg, simple)
        else:
            avg = len(positions) // 2
            break

    # loop check if -1 position is better until it's not
    while avg >= min(positions):
        if sum_total_fuel_needed(positions, avg - 1, simple) < least_fuel:
            avg -= 1
            least_fuel = sum_total_fuel_needed(positions, avg, simple)
        else:
            break

    return least_fuel


def part1(input_file):
    final_input = txt_opener(input_file, ',')
    return fuel_calculator(final_input)


def part2(input_file):
    final_input = txt_opener(input_file, ',')
    return fuel_calculator(final_input, simple=False)
            