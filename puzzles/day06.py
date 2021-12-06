from .methods import txt_opener


class Lanternfish:
    fish = []

    def __init__(self, days):
        self.cycle = days
        Lanternfish.fish.append(self)

    def live_another_day(self):
        if not self.cycle:
            self.create_new_lanternfish()
        else:
            self.cycle -= 1

    def create_new_lanternfish(self, days=8):
        self.cycle = 6
        Lanternfish(days)


def part1(input_file):
    final_input = txt_opener(input_file, ',')
    Lanternfish.fish = [Lanternfish(fishy) for fishy in final_input]
    for day in range(80):
        for fishy in Lanternfish.fish.copy():
            fishy.live_another_day()
    return len(Lanternfish.fish)


# same problem as part1 but different approach because of huge amount of calculations
def part2(input_file):
    final_input = txt_opener(input_file, ',')

    days = 256
    fish_pool = {day: 0 for day in range(days + 10)}

    for fish in final_input:
        fish_pool[fish] += 1

    while (day := min(fish_pool)) < days:
        fish_pool[day + 7] += fish_pool[day]
        fish_pool[day + 9] += fish_pool[day]
        del fish_pool[day]

    return sum(fish_pool.values())
