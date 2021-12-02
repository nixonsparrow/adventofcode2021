from ..puzzles import day15
import pytest            


@pytest.mark.ignored
class TestDay15:

    def test_part1(self):
        assert day15.part1('/../inputs/day15_test.txt') == 1
        assert day15.part1('/../inputs/day15_final.txt') == 99

    def test_part2(self):
        assert day15.part2('/../inputs/day15_test.txt') == 1
        assert day15.part2('/../inputs/day15_final.txt') == 99
            