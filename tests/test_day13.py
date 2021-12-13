from ..puzzles import day13
import pytest


@pytest.mark.finished
class TestDay13:
    def test_fold_paper(self):
        assert day13.fold_paper([(0, 0), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)],
                                {'axis': 'x', 'value': 1}) == [(0, 0), (0, 1), (0, 2)]
        assert day13.fold_paper([(0, 0), (0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                                {'axis': 'y', 'value': 1}) == [(0, 0), (1, 0), (2, 0)]

    def test_print_paper(self):
        assert day13.print_paper([(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]) == '#.#\n.#.\n#.#\n'

    def test_part1(self):
        assert day13.part1('/../inputs/day13_test.txt') == 17
        assert day13.part1('/../inputs/day13_final.txt') == 671

    # PART 2 IS BASED ON PRINTED HUMAN READABLE OUTPUT, NO NEED TO TEST IT IN THAT WAY
    # def test_part2(self):
    #     assert day13.part2('/../inputs/day13_test.txt') == 1
    #     assert day13.part2('/../inputs/day13_final.txt') == 1
