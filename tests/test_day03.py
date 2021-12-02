from ..puzzles import day03
import pytest            


@pytest.mark.ignored
class TestDay03:

    def test_part1(self):
        assert day03.part1('/../inputs/day03_test.txt') == 1
        assert day03.part1('/../inputs/day03_final.txt') == 99

    def test_part2(self):
        assert day03.part2('/../inputs/day03_test.txt') == 1
        assert day03.part2('/../inputs/day03_final.txt') == 99
            