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
        self.winning_number = None
        self.drawer = None

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
        if self.winning_number:
            return True

        winning_layouts = [''.join([str(x) for x in self.grid[row].values()]) for row in self.grid]
        [winning_layouts.append(''.join([str(self.grid[row][col]) for row in self.grid])) for col in self.bingo]
        for layout in winning_layouts:
            if layout == 'XXXXX':
                self.winning_number = self.drawer.number
                return True
        return False

    def calculate_final_score(self):
        return self.sum_unmarked_numbers() * self.winning_number if self.winning_number else None


class BingoDrawer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
        self.number = None
        self.grids = []
        self.winners = []

    def draw_next_number(self):
        self.index += 1
        self.number = self.numbers[self.index - 1]
        [grid.mark_number(self.number) for grid in self.grids]
        return self.number

    def is_grid_in_game(self, grid):
        return True if grid in self.grids else False

    def append_grids(self, grids):
        for grid in grids:
            if not self.is_grid_in_game(grid):
                self.grids.append(grid)
                grid.drawer = self

    def check_for_winner(self):
        for grid in self.grids:
            if grid.check_if_won() and grid not in self.winners:
                self.winners.append(grid)


def prepare_for_bingo(whole_list):
    numbers_drawn = [int(nr) for nr in whole_list[0].split(',')]
    raw_grids = [[whole_list[row + i] for row in range(0, 5)] for i in range(1, len(whole_list), 5)]
    grids = []
    for raw_grid in raw_grids:
        grids.append(Grid(raw_grid))

    return numbers_drawn, grids


def part1(input_file=''):
    final_input = txt_opener(input_file, '\n')
    numbers_drawn, grids = prepare_for_bingo(final_input)

    drawer = BingoDrawer(numbers_drawn)
    drawer.append_grids([grid for grid in grids])

    while not drawer.winners:
        drawer.draw_next_number()
        drawer.check_for_winner()

    return drawer.winners[0].calculate_final_score()


def part2(input_file=''):
    final_input = txt_opener(input_file, '\n')
    numbers_drawn, grids = prepare_for_bingo(final_input)

    drawer = BingoDrawer(numbers_drawn)
    drawer.append_grids([grid for grid in grids])

    while len(drawer.winners) != len(drawer.grids):
        drawer.draw_next_number()
        drawer.check_for_winner()

    return drawer.winners[-1].calculate_final_score()
            