from ..puzzles import day08
import pytest            


@pytest.mark.ignored
class TestDay08:

    def test_part1(self):
        assert day08.part1('/../inputs/day08_test.txt') == 1
        assert day08.part1('/../inputs/day08_final.txt') == 99

    def test_part2(self):
        assert day08.part2('/../inputs/day08_test.txt') == 1
        assert day08.part2('/../inputs/day08_final.txt') == 99
            