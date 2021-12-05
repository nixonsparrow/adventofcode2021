from ..puzzles import day04, methods
import pytest            


class TestDay04:
    @pytest.fixture()
    def include_drawer(self):
        self.drawer = day04.BingoDrawer([nr for nr in range(25)])

    @pytest.fixture()
    def create_grid_default(self, include_drawer):      # Creates default grid with numbers 0-24
        self.default_grid = day04.Grid()
        self.drawer.append_grids([self.default_grid])

    @pytest.fixture()
    def create_grid_test(self, include_drawer):         # Creates grid with test values
        numbers_drawn, grids = day04.prepare_for_bingo(methods.txt_opener('/../inputs/day04_test.txt', '\n'))
        self.test_grid = grids[0]
        self.drawer.append_grids([self.test_grid])

    def test_prepare_numbers_drawn(self):
        numbers_drawn, grids = day04.prepare_for_bingo(methods.txt_opener('/../inputs/day04_test.txt', '\n'))
        assert len(numbers_drawn) == 27
        assert numbers_drawn[0] == 7

    def test_create_bingo_grid_from_input(self, create_grid_test):
        b, i, n, g, o = day04.Grid.bingo
        assert self.test_grid.grid[0][b] == 22
        assert self.test_grid.grid[0][i] == 13
        assert self.test_grid.grid[0][n] == 17
        assert self.test_grid.grid[0][g] == 11
        assert self.test_grid.grid[0][o] == 0

    def test_grid_check_for_number(self, create_grid_default):
        assert self.default_grid.check_for_number(0)
        assert self.default_grid.check_for_number(24)
        assert not self.default_grid.check_for_number(99)

    def test_count_unmarked_numbers(self, create_grid_test, create_grid_default):
        assert self.test_grid.sum_unmarked_numbers() == 300     # sum of 0-24
        assert self.default_grid.sum_unmarked_numbers() == 300

        self.test_grid.mark_number(24)              # number that is on both grids
        self.default_grid.mark_number(24)           # is marked, so should change the sum
        assert self.test_grid.sum_unmarked_numbers() == 276
        assert self.default_grid.sum_unmarked_numbers() == 276

        self.test_grid.mark_number(99)              # number that is not on neither grids
        self.default_grid.mark_number(99)
        assert self.test_grid.sum_unmarked_numbers() == 276
        assert self.default_grid.sum_unmarked_numbers() == 276

    def test_number_drawing(self, include_drawer):
        assert self.drawer.draw_next_number() == 0
        assert self.drawer.draw_next_number() == 1
        assert self.drawer.draw_next_number() == 2

    def test_number_drawn_crossed(self, create_grid_test, create_grid_default, include_drawer):
        self.drawer.append_grids([self.test_grid, self.default_grid])
        assert self.drawer.draw_next_number() == 0
        assert self.test_grid.check_for_number(0) is False
        assert self.default_grid.check_for_number(0) is False

    def test_is_grid_in_game(self, create_grid_default, include_drawer):
        self.drawer.append_grids([self.default_grid])
        assert self.drawer.is_grid_in_game(self.default_grid)

    def test_check_if_won_horizontal(self, create_grid_default):
        assert self.default_grid.check_if_won() is False
        for x in day04.Grid.bingo:
            self.default_grid.grid[1][x] = 'X'
        assert self.default_grid.check_if_won() is True

    def test_check_if_won_vertical(self, create_grid_default):
        assert self.default_grid.check_if_won() is False
        for x in range(5):
            self.default_grid.grid[x][day04.Grid.bingo[1]] = 'X'
        assert self.default_grid.check_if_won() is True

    def test_calculate_final_score(self, create_grid_default):
        assert self.default_grid.calculate_final_score() is None    # No winning number
        self.default_grid.winning_number = 2
        assert self.default_grid.calculate_final_score() == 600

    def test_part1(self):
        assert day04.part1('/../inputs/day04_test.txt') == 4512
        assert day04.part1('/../inputs/day04_final.txt') == 33348

    def test_part2(self):
        assert day04.part2('/../inputs/day04_test.txt') == 1924
        assert day04.part2('/../inputs/day04_final.txt') == 8112
