from ..puzzles import day06
import pytest            


@pytest.mark.ignored
class TestDay06:

    def test_part1(self):
        assert day06.part1('/../inputs/day06_test.txt') == 1
        assert day06.part1('/../inputs/day06_final.txt') == 99

    def test_part2(self):
        assert day06.part2('/../inputs/day06_test.txt') == 1
        assert day06.part2('/../inputs/day06_final.txt') == 99
            