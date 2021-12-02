from ..puzzles import day24
import pytest            


@pytest.mark.ignored
class TestDay24:

    def test_part1(self):
        assert day24.part1('/../inputs/day24_test.txt') == 1
        assert day24.part1('/../inputs/day24_final.txt') == 99

    def test_part2(self):
        assert day24.part2('/../inputs/day24_test.txt') == 1
        assert day24.part2('/../inputs/day24_final.txt') == 99
            