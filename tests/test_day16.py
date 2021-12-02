from ..puzzles import day16
import pytest            


@pytest.mark.ignored
class TestDay16:

    def test_part1(self):
        assert day16.part1('/../inputs/day16_test.txt') == 1
        assert day16.part1('/../inputs/day16_final.txt') == 99

    def test_part2(self):
        assert day16.part2('/../inputs/day16_test.txt') == 1
        assert day16.part2('/../inputs/day16_final.txt') == 99
            