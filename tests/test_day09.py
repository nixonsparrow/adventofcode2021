from ..puzzles import day09
import pytest            


@pytest.mark.ignored
class TestDay09:

    def test_part1(self):
        assert day09.part1('/../inputs/day09_test.txt') == 1
        assert day09.part1('/../inputs/day09_final.txt') == 99

    def test_part2(self):
        assert day09.part2('/../inputs/day09_test.txt') == 1
        assert day09.part2('/../inputs/day09_final.txt') == 99
            