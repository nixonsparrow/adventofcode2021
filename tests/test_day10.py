from ..puzzles import day10
import pytest            


@pytest.mark.ignored
class TestDay10:

    def test_part1(self):
        assert day10.part1('/../inputs/day10_test.txt') == 1
        assert day10.part1('/../inputs/day10_final.txt') == 99

    def test_part2(self):
        assert day10.part2('/../inputs/day10_test.txt') == 1
        assert day10.part2('/../inputs/day10_final.txt') == 99
            