from ..puzzles import day19
import pytest            


@pytest.mark.ignored
class TestDay19:

    def test_part1(self):
        assert not day19.part1('/../inputs/day19_test.txt')
        assert not day19.part1('/../inputs/day19_final.txt')

    def test_part2(self):
        assert not day19.part2('/../inputs/day19_test.txt')
        assert not day19.part2('/../inputs/day19_final.txt')
            