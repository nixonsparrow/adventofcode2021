from ..puzzles import day05
import pytest


@pytest.mark.finished
class TestDay05:
    @pytest.fixture()
    def create_map(self):
        self.map = day05.Map()

    def test_drawing_straight_line(self, create_map):
        self.map.draw_line('0,9', '5,9')
        assert all([self.map.array[9][x] for x in range(0, 6)])
        assert not any([self.map.array[9][x] for x in range(6, 10)])
        assert not any([self.map.array[y][x] for y in range(0, 9) for x in range(0, 10)])

    def test_drawing_diagonal_line(self, create_map):
        self.map.draw_line('8,9', '9,8')
        assert all([self.map.array[9][8], self.map.array[8][9]])
        assert not any([self.map.array[9][9], self.map.array[8][8]])
        assert not any([self.map.array[y][x] for y in range(0, 8) for x in range(0, 8)])

    def test_count_crossings(self, create_map):
        assert not self.map.count_crossings()
        self.map.draw_line('0,9', '5,9')
        self.map.draw_line('5,7', '5,9')
        assert self.map.count_crossings()

    def test_part1(self):
        assert day05.part1('/../inputs/day05_test.txt') == 5
        assert day05.part1('/../inputs/day05_final.txt') == 5306

    def test_part2(self):
        assert day05.part2('/../inputs/day05_test.txt') == 12
        assert day05.part2('/../inputs/day05_final.txt') == 17787
            