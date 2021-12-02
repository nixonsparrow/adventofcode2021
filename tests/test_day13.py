from ..puzzles import day13
import pytest            


@pytest.mark.ignored
class TestDay13:

    def test_part1(self):
        assert day13.part1('/../inputs/day13_test.txt') == 1
        assert day13.part1('/../inputs/day13_final.txt') == 99

    def test_part2(self):
        assert day13.part2('/../inputs/day13_test.txt') == 1
        assert day13.part2('/../inputs/day13_final.txt') == 99
            