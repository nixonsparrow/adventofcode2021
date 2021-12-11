from ..puzzles import day11
import pytest


@pytest.mark.finished
class TestDay11:
    def test_dumbos_flash_festival(self):
        assert day11.dumbos_flash_festival([[9, 0], [0, 9]], [(0, 0), (1, 1)]) == ([[0, 0], [0, 0]], 2)
        assert day11.dumbos_flash_festival([[9, 8], [7, 6]], [(0, 0)]) == ([[0, 8], [7, 6]], 1)
        assert day11.dumbos_flash_festival([[9, 8, 9], [7, 6, 4], [5, 4, 2]], [(0, 0), (0, 2)]) ==\
                                          ([[0, 8, 0], [7, 6, 4], [5, 4, 2]], 2)

    def test_search_for_flashes(self):
        assert day11.search_for_flashes([[9, 9], [0, 0]]) == ([[9, 9], [0, 0]], [])
        assert day11.search_for_flashes([[9, 10], [0, 0]]) == ([[11, 12], [2, 2]], [(0, 1), (0, 0)])

    def test_grid_change_after_one_step(self):
        assert day11.go_one_step([[9, 0], [0, 9]]) == ([[0, 3], [3, 0]], 2)     # grid + flashes
        assert day11.go_one_step([[8, 8, 9], [7, 6, 4], [5, 4, 2]]) ==\
                                ([[0, 0, 0], [0, 0, 8], [8, 7, 4]], 5)

    def test_part1(self):
        assert day11.part1('/../inputs/day11_test.txt') == 1656
        assert day11.part1('/../inputs/day11_final.txt') == 1681

    def test_part2(self):
        assert day11.part2('/../inputs/day11_test.txt') == 195
        assert day11.part2('/../inputs/day11_final.txt') == 276
