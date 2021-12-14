from ..puzzles import day14
import pytest


class TestDay14:
    def test_polymer_insertion(self):
        assert day14.polymer_insertion('ABCD', {'AB': 'E', 'CD': 'F'}) == 'AEBCFD'

    def test_get_occurrences(self):
        assert day14.get_occurrences('AAAA') == [{'letter': 'A', 'total': 4}]
        assert day14.get_occurrences('CAABBDAACCBBA') == [
            {'letter': 'A', 'total': 5}, {'letter': 'B', 'total': 4},
            {'letter': 'C', 'total': 3}, {'letter': 'D', 'total': 1},
        ]

    def test_part1(self):
        assert day14.part1('/../inputs/day14_test.txt') == 1588
        assert day14.part1('/../inputs/day14_final.txt') == 2447

    @pytest.mark.skip
    def test_part2(self):
        assert day14.part2('/../inputs/day14_test.txt') == 2188189693529
        assert day14.part2('/../inputs/day14_final.txt') == 1
