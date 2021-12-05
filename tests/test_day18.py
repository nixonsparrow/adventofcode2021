from ..puzzles import day18
import pytest            


@pytest.mark.ignored
class TestDay18:

    def test_part1(self):
        assert not day18.part1('/../inputs/day18_test.txt')
        assert not day18.part1('/../inputs/day18_final.txt')

    def test_part2(self):
        assert not day18.part2('/../inputs/day18_test.txt')
        assert not day18.part2('/../inputs/day18_final.txt')
            