from ..puzzles import day24
import pytest


class TestDay24:
    def test_command_add(self):
        assert day24.cmd_add(2, 4) == 6

    def test_command_multiply(self):
        assert day24.cmd_mul(2, 4) == 8

    def test_command_divide(self):
        assert day24.cmd_div(4, 2) == 2
        assert day24.cmd_div(5, 2) == 2

    def test_command_modulo(self):
        assert day24.cmd_mod(4, 2) == 0
        assert day24.cmd_mod(5, 2) == 1

    def test_command_equal(self):
        assert day24.cmd_eql(2, 2) == 1
        assert day24.cmd_eql(5, 2) == 0

    # def test_part1(self):
    #     assert not day24.part1('/../inputs/day24_test.txt')
    #     assert not day24.part1('/../inputs/day24_final.txt')
    #
    # def test_part2(self):
    #     assert not day24.part2('/../inputs/day24_test.txt')
    #     assert not day24.part2('/../inputs/day24_final.txt')
            