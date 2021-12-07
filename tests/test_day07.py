from ..puzzles import day07
import pytest


class TestDay07:

    def test_total_fuel_needed(self):
        assert day07.sum_total_fuel_needed([1, 2, 3], 2) == 2
        assert day07.sum_total_fuel_needed([1, 2, 3, 4, 5], 3) == 6
        assert day07.sum_total_fuel_needed([1, 2, 3, 4, 5], 2) == 7
        assert day07.sum_total_fuel_needed([1, 2, 3], 2, that_simple=False) == 2
        assert day07.sum_total_fuel_needed([1, 2, 3, 4, 5], 3, that_simple=False) == 8
        assert day07.sum_total_fuel_needed([1, 2, 3, 4, 5], 2, that_simple=False) == 11

    def test_fuel_calculator_simple(self):
        assert day07.fuel_calculator([1, 2, 3]) == 2
        assert day07.fuel_calculator([1, 2, 3, 4, 5]) == 6

    def test_fuel_calculator_not_that_simple(self):
        assert day07.fuel_calculator([1, 2, 3], simple=False) == 2
        assert day07.fuel_calculator([1, 2, 3, 4, 5], simple=False) == 8

    def test_part1(self):
        assert day07.part1('/../inputs/day07_test.txt') == 37
        assert day07.part1('/../inputs/day07_final.txt') == 335271

    def test_part2(self):
        assert day07.part2('/../inputs/day07_test.txt') == 168
        assert day07.part2('/../inputs/day07_final.txt') == 95851339
            