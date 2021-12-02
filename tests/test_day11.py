from ..puzzles import day11
import pytest            


@pytest.mark.ignored
class TestDay11:

    def test_part1(self):
        assert day11.part1('/../inputs/day11_test.txt') == 1
        assert day11.part1('/../inputs/day11_final.txt') == 99

    def test_part2(self):
        assert day11.part2('/../inputs/day11_test.txt') == 1
        assert day11.part2('/../inputs/day11_final.txt') == 99
            