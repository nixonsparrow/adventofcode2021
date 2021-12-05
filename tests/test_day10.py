from ..puzzles import day10
import pytest            


@pytest.mark.ignored
class TestDay10:

    def test_part1(self):
        assert not day10.part1('/../inputs/day10_test.txt')
        assert not day10.part1('/../inputs/day10_final.txt')

    def test_part2(self):
        assert not day10.part2('/../inputs/day10_test.txt')
        assert not day10.part2('/../inputs/day10_final.txt')
            