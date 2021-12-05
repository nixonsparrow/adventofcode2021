from ..puzzles import day23
import pytest            


@pytest.mark.ignored
class TestDay23:

    def test_part1(self):
        assert not day23.part1('/../inputs/day23_test.txt')
        assert not day23.part1('/../inputs/day23_final.txt')

    def test_part2(self):
        assert not day23.part2('/../inputs/day23_test.txt')
        assert not day23.part2('/../inputs/day23_final.txt')
            