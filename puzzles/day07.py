from .methods import txt_opener


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


def compare_with_next(positions, least_fuel, simple, descending=False):
    avg = len(positions)//2
    # loop check if +1/-1 position is better until it's not
    while avg >= min(positions) if descending else avg <= max(positions):
        if sum_total_fuel_needed(positions, avg - 1 if descending else avg + 1, simple) <= least_fuel:
            avg += - 1 if descending else 1
            least_fuel = sum_total_fuel_needed(positions, avg, simple)
        else:
            return least_fuel
    return least_fuel


# calculate least possible fuel needed
def fuel_calculator(positions, simple=True):
    # get rounded average position
    avg = len(positions)//2
    least_fuel = sum_total_fuel_needed(positions, avg, simple)

    least_fuel = compare_with_next(positions, least_fuel, simple)
    least_fuel = compare_with_next(positions, least_fuel, simple, descending=True)

    return least_fuel


def part1(input_file):
    final_input = txt_opener(input_file, ',')
    return fuel_calculator(final_input)


def part2(input_file):
    final_input = txt_opener(input_file, ',')
    return fuel_calculator(final_input, simple=False)
            