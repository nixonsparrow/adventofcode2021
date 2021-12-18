from ..puzzles import day17
import pytest


@pytest.mark.finished
class TestDay17:
    target = ((20, 30), (-10, -5))
    trajectory = [(0, 0), (7, 2), (13, 3), (18, 3), (22, 2), (25, 0), (27, -3), (28, -7)]

    def test_read_target_area(self):
        assert day17.read_target_area('target area: x=20..30, y=-10..-5') == ((20, 30), (-10, -5))
        assert day17.read_target_area('target area: x=195..238, y=-93..-67') == ((195, 238), (-93, -67))

    def test_calculate_trajectory(self):
        assert day17.calculate_trajectory(7, 2, self.target) == self.trajectory
        assert day17.calculate_trajectory(9, 0, self.target) == [(0, 0), (9, 0), (17, -1), (24, -3), (30, -6)]

    def test_get_highest_position(self):
        assert day17.get_highest_position(self.trajectory) == 3

    def test_get_xs_that_may_hit(self):
        assert day17.get_xs_that_may_hit(self.target) == [6, 7]

    def test_check_if_probe_hits_target(self):
        for x, y in [(25, -7), (20, -5), (25, -7)]:
            assert day17.check_if_probe_hits_target(x, y, self.target)

    def test_check_if_probe_does_not_hit_target(self):
        for x, y in [(19, -8), (-10, 25), (17, -4)]:
            assert not day17.check_if_probe_hits_target(x, y, self.target)

    def test_part1(self):
        assert day17.part1('/../inputs/day17_test.txt') == 45
        assert day17.part1('/../inputs/day17_final.txt') == 4278

    def test_part2(self):
        assert day17.part2('/../inputs/day17_test.txt') == 112
        assert day17.part2('/../inputs/day17_final.txt') == 1994
            