from ..puzzles import day16
import pytest


class TestDay16:
    def test_get_bin(self):
        assert day16.get_bin(0) == '0000'
        assert day16.get_bin(5) == '0101'
        assert day16.get_bin('F') == '1111'

    def test_translate_into_binary(self):
        assert day16.translate_into_binary('D2FE28') == '110100101111111000101000'
        assert day16.translate_into_binary('38006F45291200') == '00111000000000000110111101000101001010010001001000000000'
        assert day16.translate_into_binary('EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000'

    def test_get_id(self):
        assert day16.get_id('110100101111111000101000') == 4
        assert day16.get_id('00111000000000000110111101000101001010010001001000000000') == 6
        assert day16.get_id('11101110000000001101010000001100100000100011000001100000') == 3

    def test_get_version(self):
        assert day16.get_version('110100101111111000101000') == 6
        assert day16.get_version('00111000000000000110111101000101001010010001001000000000') == 1
        assert day16.get_version('11101110000000001101010000001100100000100011000001100000') == 7

    # def test_part1(self):
    #     results = [16, 12, 23, 31]
    #     for nr in range(4):
    #         assert day16.part1(f'/../inputs/day16_test{nr + 1}.txt') == results[nr]
    #     assert not day16.part1('/../inputs/day16_final.txt')
# 
#     def test_part2(self):
#         assert not day16.part2('/../inputs/day16_test1.txt')
#         assert not day16.part2('/../inputs/day16_final.txt')
            