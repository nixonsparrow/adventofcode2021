from ..puzzles import day18
import pytest            


@pytest.mark.ignored
class TestDay18:

    def test_part1(self):
        assert day18.part1('/../inputs/day18_test.txt') == 1
        assert day18.part1('/../inputs/day18_final.txt') == 99

    def test_part2(self):
        assert day18.part2('/../inputs/day18_test.txt') == 1
        assert day18.part2('/../inputs/day18_final.txt') == 99
            