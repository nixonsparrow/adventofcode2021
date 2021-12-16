from ..puzzles import day15
import pytest


@pytest.mark.finished
class TestDay15:
    def test_adjacent(self):
        assert list(day15.adjacent((0, 0), ['1234', '5678'])) == [(1, 0), (0, 1)]

    def test_enlarge_grid(self):
        assert day15.enlarge_grid(['567']) == ['567678789891912',
                                               '678789891912123',
                                               '789891912123234',
                                               '891912123234345',
                                               '912123234345456']

    def test_part1(self):
        assert day15.part1('/../inputs/day15_test.txt') == 40
        assert day15.part1('/../inputs/day15_final.txt') == 447

    def test_part2(self):
        assert day15.part2('/../inputs/day15_test.txt') == 315
        assert day15.part2('/../inputs/day15_final.txt') == 2825
