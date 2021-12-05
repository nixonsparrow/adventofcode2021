from ..puzzles import day08
import pytest            


@pytest.mark.ignored
class TestDay08:

    def test_part1(self):
        assert not day08.part1('/../inputs/day08_test.txt')
        assert not day08.part1('/../inputs/day08_final.txt')

    def test_part2(self):
        assert not day08.part2('/../inputs/day08_test.txt')
        assert not day08.part2('/../inputs/day08_final.txt')
            