from ..puzzles import day04
import pytest            


@pytest.mark.ignored
class TestDay04:

    def test_part1(self):
        assert day04.part1('/../inputs/day04_test.txt') == 1
        assert day04.part1('/../inputs/day04_final.txt') == 99

    def test_part2(self):
        assert day04.part2('/../inputs/day04_test.txt') == 1
        assert day04.part2('/../inputs/day04_final.txt') == 99
            