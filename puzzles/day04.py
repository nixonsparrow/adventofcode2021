from .methods import txt_opener


class Grid:
    bingo = 'BINGO'

    def __init__(self, grid=None):
        if grid:
            self.grid = {row: {self.bingo[i]: int(grid[row].split()[i]) for i in range(5)} for row in range(5)}
        else:
            self.grid = {row: {self.bingo[i]: None for i in range(5)} for row in range(5)}
            x = 0
            for z in range(5):
                for y in range(5):
                    self.grid[z][self.bingo[y]] = x
                    x += 1

        self.grid_sum = None

    def check_for_number(self, nr):
        for row in self.grid:
            for letter in self.bingo:
                if self.grid[row][letter] == nr:
                    return letter, row
        return False

    def mark_number(self, nr):
        if self.check_for_number(nr):
            letter, row = self.check_for_number(nr)
            self.grid[row][letter] = 'X'

    def sum_unmarked_numbers(self):
        return sum([sum(x for x in row.values() if type(x) == int) for row in self.grid.values()])

    def check_if_won(self):              # collect every row then every column
        winning_layouts = [''.join([str(x) for x in self.grid[row].values()]) for row in self.grid]
        [winning_layouts.append(''.join([str(self.grid[row][col]) for row in self.grid])) for col in 'BINGO']
        for layout in winning_layouts:
            if layout == 'XXXXX':
                return True
        return False

    def calculate_final_score(self, winning_number):
        return self.sum_unmarked_numbers() * winning_number


class BingoDrawer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
        self.current_number = None
        self.grids = []

    def draw_next_number(self):
        self.index += 1
        number = self.numbers[self.index - 1]
        [grid.mark_number(number) for grid in self.grids]
        return (number, None) if not self.check_for_winner() else (self.check_for_winner(), number)

    def is_grid_in_game(self, grid):
        return True if grid in self.grids else False

    def append_grids(self, grids):
        for grid in grids:
            self.grids.append(grid) if not self.is_grid_in_game(grid) else None

    def check_for_winner(self):
        for grid in self.grids:
            if grid.check_if_won():
                return grid
        return None


def prepare_for_bingo(whole_list):
    numbers_drawn = [int(nr) for nr in whole_list[0].split(',')]
    raw_grids = [[whole_list[row + i] for row in range(1, 6)] for i in range(1, len(whole_list), 6)]
    grids = []
    for raw_grid in raw_grids:
        grids.append(Grid(raw_grid))

    return numbers_drawn, grids


def part1(input_file=''):
    final_input = txt_opener(input_file, '\n')
    numbers_drawn, grids = prepare_for_bingo(final_input)

    drawer = BingoDrawer(numbers_drawn)
    [drawer.grids.append(grid) for grid in grids]

    winner, last_number = None, None
    while type(winner) != Grid:
        winner, last_number = drawer.draw_next_number()

    print(winner.sum_unmarked_numbers(), last_number)
    return winner.calculate_final_score(last_number)


def part2(input_file=''):
    final_input = txt_opener(input_file, '\n')
    return final_input
            