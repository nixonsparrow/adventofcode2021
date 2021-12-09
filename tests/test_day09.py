from ..puzzles import day09
import pytest


@pytest.mark.finished
class TestDay09:
    heightmap = [[9, 1, 9, 2],
                 [1, 0, 9, 1],
                 [9, 1, 9, 2]]

    def test_is_low_point(self):
        assert day09.is_low_point(self.heightmap, 1, 1)
        assert day09.is_low_point(self.heightmap, 1, 3)
        assert not day09.is_low_point(self.heightmap, 2, 3)

    def test_get_low_points(self):
        assert day09.get_low_points(self.heightmap) == {(1, 1): 0, (1, 3): 1}

    def test_get_basin(self):
        assert day09.get_basin((1, 1), self.heightmap) == [(1, 1), (1, 0), (0, 1), (2, 1)]
        assert day09.get_basin((1, 3), self.heightmap) == [(1, 3), (0, 3), (2, 3)]

    def test_multiple_3_biggest_basins(self):
        assert day09.multiple_3_biggest_basins([2, 8, 6, 3, 10]) == 480

    def test_part1(self):
        assert day09.part1('/../inputs/day09_test.txt') == 15
        assert day09.part1('/../inputs/day09_final.txt') == 494

    def test_part2(self):
        assert day09.part2('/../inputs/day09_test.txt') == 1134
        assert day09.part2('/../inputs/day09_final.txt') == 1048128
            