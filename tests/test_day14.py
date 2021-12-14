from ..puzzles import day14
import pytest


@pytest.mark.finished
class TestDay14:
    def test_polymer_insertion(self):
        assert day14.polymer_insertion('ABCD', {'AB': 'E', 'CD': 'F'}) == 'AEBCFD'

    def test_get_occurrences(self):
        assert day14.get_occurrences('AAAA') == [{'letter': 'A', 'total': 4}]
        assert day14.get_occurrences('CAABBDAACCBBA') == [
            {'letter': 'A', 'total': 5}, {'letter': 'B', 'total': 4},
            {'letter': 'C', 'total': 3}, {'letter': 'D', 'total': 1},
        ]

    def test_get_letter_occurrences(self):
        assert day14.get_letter_occurrences(
            {'A': 0, 'B': 0}, {'AB': 2, 'BA': 2}, 'A') == {'A': 3, 'B': 2}      # ABABA
        assert day14.get_letter_occurrences({'A': 0, 'B': 0, 'C': 0},           # ABCCBA
            {'AB': 1, 'BA': 1, 'CB': 1, 'BC': 1, 'CC': 1}, 'A') == {'A': 2, 'B': 2, 'C': 2}

    def test_update_polymer_dictionary(self):
        assert day14.update_polymer_dictionary({'AB': 1, 'BC': 1, 'BB': 0}, {'AB': 'B', 'BC': 'B'}
                                               ) == {'AB': 1, 'BC': 1, 'BB': 2}

    def test_part1(self):
        assert day14.part1('/../inputs/day14_test.txt') == 1588
        assert day14.part1('/../inputs/day14_final.txt') == 2447

    def test_part2(self):
        assert day14.part2('/../inputs/day14_test.txt') == 2188189693529
        assert day14.part2('/../inputs/day14_final.txt') == 3018019237563
