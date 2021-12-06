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


def part2(input_file):
    # final_input = txt_opener(input_file, ',')
    #
    # Lanternfish.fish = [Lanternfish(fishy) for fishy in final_input]
    #
    # x = [8, 16, 24]
    # for y in x:
    #     Lanternfish.fish = []
    #     for day in range(8):
    #         for fishy in Lanternfish.fish.copy():
    #             fishy.live_another_day()
    #     print(len(Lanternfish.fish))

    return None
            