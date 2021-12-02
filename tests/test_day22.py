from ..puzzles import day22
import pytest            


@pytest.mark.ignored
class TestDay22:

    def test_part1(self):
        assert day22.part1('/../inputs/day22_test.txt') == 1
        assert day22.part1('/../inputs/day22_final.txt') == 99

    def test_part2(self):
        assert day22.part2('/../inputs/day22_test.txt') == 1
        assert day22.part2('/../inputs/day22_final.txt') == 99
            