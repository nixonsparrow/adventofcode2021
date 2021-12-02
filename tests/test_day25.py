from ..puzzles import day25
import pytest            


@pytest.mark.ignored
class TestDay25:

    def test_part1(self):
        assert day25.part1('/../inputs/day25_test.txt') == 1
        assert day25.part1('/../inputs/day25_final.txt') == 99

    def test_part2(self):
        assert day25.part2('/../inputs/day25_test.txt') == 1
        assert day25.part2('/../inputs/day25_final.txt') == 99
            