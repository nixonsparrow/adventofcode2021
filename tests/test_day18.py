from ..puzzles import day18
import pytest


@pytest.mark.skip
class TestDay18:
    nests_ex = ['[[[[[9,8],1],2],3],4]', '[7,[6,[5,[4,[3,2]]]]]', '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]',
             '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]']
    nests_sp = ['[13,[2,2]]', '[[[2,3],12],[1,3]]']

    def test_sum_nests(self):
        assert day18.sum_nests('[[2,3],4]', '[2,2]') == '[[[2,3],4],[2,2]]'

    # def test_explode_nest(self):
        # assert day18.explode_nest(self.nests_ex[0]) == '[[[[0,9],2],3],4]'
        # assert day18.explode_nest(self.nests_ex[1]) == '[7,[6,[5,[7,0]]]]'
        # assert day18.explode_nest(self.nests_ex[2]) == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
        # assert day18.explode_nest(self.nests_ex[3]) == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
        #

    def test_special(self):
        assert day18.explode_nest('[[[[[0,0],2]],[[[[10,5]]],9]') == '[[[[0,2]],[[[[10,5]]],9]'
        assert day18.explode_nest('[[[[[0,2]],[10,5]],9],4]') == '[[[0,[12,5]],9],4]'
        assert day18.split_nest('[[[0,[12,5]],9],4]') == '[[[0,[[6,6],5]],9],4]'
        assert day18.explode_nest('[[[0,[[6,6],5]],9],4]') == '[[[6,[0,11]],9],4]'
        assert day18.split_nest('[[[6,[0,11]],9],4]') == '[[[6,[0,[6,5]]],9],4]'
        assert day18.explode_nest('[[[6,[0,[6,5]]],9],4]') == '[[[6,[6,0]],14],4]'
        assert day18.split_nest('[[[6,[6,0]],14],4]') == '[[[6,[6,0]],[7,7]],4]'
        assert not day18.explode_nest('[[[6,[6,0]],[7,7]],4]')

    def test_split_nest(self):
        assert day18.split_nest(self.nests_sp[0]) == '[[7,6],[2,2]]'
        assert day18.split_nest(self.nests_sp[1]) == '[[[2,3],[6,6]],[1,3]]'

    def test_explode_index(self):
        assert day18.explode_index(self.nests_ex[0]) == 4
        assert day18.explode_index(self.nests_ex[1]) == 12
        assert day18.explode_index(self.nests_ex[2]) == 10
        assert day18.explode_index(self.nests_ex[3]) == 24

        assert not day18.explode_index(self.nests_sp[0])

    def test_split_index(self):
        assert day18.split_index(self.nests_sp[0]) == 1
        assert day18.split_index(self.nests_sp[1]) == 8

        assert not day18.split_index(self.nests_ex[0])

    def test_part1(self):
        assert day18.part1('/../inputs/day18_test.txt') == '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
    #     assert not day18.part1('/../inputs/day18_final.txt')

    # def test_part2(self):
    #     assert not day18.part2('/../inputs/day18_test.txt')
    #     assert not day18.part2('/../inputs/day18_final.txt')
