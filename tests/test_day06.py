from ..puzzles import day06
import pytest            


@pytest.mark.ignored
class TestDay06:

    def test_part1(self):
        assert not day06.part1('/../inputs/day06_test.txt')
        assert not day06.part1('/../inputs/day06_final.txt')

    def test_part2(self):
        assert not day06.part2('/../inputs/day06_test.txt')
        assert not day06.part2('/../inputs/day06_final.txt')
            