from ..puzzles import day22
import pytest


class TestDay22:

    def test_part1(self):
        assert day22.part1('/../inputs/day22_test.txt') == 590784
        assert day22.part1('/../inputs/day22_test2.txt') == 474140
        assert day22.part1('/../inputs/day22_final.txt') == 503864

    @pytest.mark.skip
    def test_part2(self):
        assert day22.part2('/../inputs/day22_test2.txt') == 2758514936282235
        assert day22.part2('/../inputs/day22_final.txt') == 1
            