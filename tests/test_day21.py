from ..puzzles import day21
import pytest            


@pytest.mark.ignored
class TestDay21:

    def test_part1(self):
        assert day21.part1('/../inputs/day21_test.txt') == 1
        assert day21.part1('/../inputs/day21_final.txt') == 99

    def test_part2(self):
        assert day21.part2('/../inputs/day21_test.txt') == 1
        assert day21.part2('/../inputs/day21_final.txt') == 99
            