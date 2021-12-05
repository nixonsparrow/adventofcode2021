from ..puzzles import day12
import pytest            


@pytest.mark.ignored
class TestDay12:

    def test_part1(self):
        assert not day12.part1('/../inputs/day12_test.txt')
        assert not day12.part1('/../inputs/day12_final.txt')

    def test_part2(self):
        assert not day12.part2('/../inputs/day12_test.txt')
        assert not day12.part2('/../inputs/day12_final.txt')
            