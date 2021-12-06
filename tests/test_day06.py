from ..puzzles import day06
import pytest            


class TestDay06:

    def test_part1(self):
        assert day06.part1('/../inputs/day06_test.txt') == 5934
        assert day06.part1('/../inputs/day06_final.txt') == 365131

    def test_part2(self):
        assert day06.part2('/../inputs/day06_test.txt') == 26984457539
        # assert day06.part2('/../inputs/day06_final.txt') == 26984457539
            