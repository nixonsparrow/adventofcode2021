from ..puzzles import day10
import pytest


class TestDay10:
    def test_autocomplete_tool(self):
        assert day10.autocomplete_tool('<{([') == 294

    def test_search_for_bracket_closure(self):
        assert day10.search_for_bracket_closures('{}') == ''
        assert day10.search_for_bracket_closures('[{)}') == 3        # ) - first wrong closure
        assert day10.search_for_bracket_closures('[{]}') == 57       # ] - first wrong closure
        assert day10.search_for_bracket_closures('[{}}') == 1197     # } - first wrong closure
        assert day10.search_for_bracket_closures('[{>}') == 25137    # > - first wrong closure

    def test_part1(self):
        assert day10.part1('/../inputs/day10_test.txt') == 26397
        assert day10.part1('/../inputs/day10_final.txt') == 392367

    def test_part2(self):
        assert day10.part2('/../inputs/day10_test.txt') == 288957
        assert day10.part2('/../inputs/day10_final.txt') == 2192104158
            