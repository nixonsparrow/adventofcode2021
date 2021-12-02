from ..puzzles import day05
import pytest            


@pytest.mark.ignored
class TestDay05:

    def test_part1(self):
        assert day05.part1('/../inputs/day05_test.txt') == 1
        assert day05.part1('/../inputs/day05_final.txt') == 99

    def test_part2(self):
        assert day05.part2('/../inputs/day05_test.txt') == 1
        assert day05.part2('/../inputs/day05_final.txt') == 99
            