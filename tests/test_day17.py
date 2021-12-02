from ..puzzles import day17
import pytest            


@pytest.mark.ignored
class TestDay17:

    def test_part1(self):
        assert day17.part1('/../inputs/day17_test.txt') == 1
        assert day17.part1('/../inputs/day17_final.txt') == 99

    def test_part2(self):
        assert day17.part2('/../inputs/day17_test.txt') == 1
        assert day17.part2('/../inputs/day17_final.txt') == 99
            