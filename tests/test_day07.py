from ..puzzles import day07
import pytest            


@pytest.mark.ignored
class TestDay07:

    def test_part1(self):
        assert not day07.part1('/../inputs/day07_test.txt')
        assert not day07.part1('/../inputs/day07_final.txt')

    def test_part2(self):
        assert not day07.part2('/../inputs/day07_test.txt')
        assert not day07.part2('/../inputs/day07_final.txt')
            