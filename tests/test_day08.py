from ..puzzles import day08
import pytest            


class TestDay08:
    dict = {
        '1': 'cf',
        '2': 'acdeg',
        '3': 'acdfg',
        '4': 'bcdf',
        '5': 'abdfg',
        '6': 'abdefg',
        '7': 'acf',
        '8': 'abcdefg',
        '9': 'abcdfg',
        '0': 'abcefg'
    }

    def test_get_same_bars(self):
        assert day08.get_same_bars('abcd', 'bcda') == 4
        assert day08.get_same_bars('abcd', 'bcda') == len('abcd')
        assert day08.get_same_bars('abch', 'bcda') == 3
        assert day08.get_same_bars('abcdefghij', 'ightfkosw') == 4

    def test_get_four_digit_code(self):
        assert day08.get_four_digit_code('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab',
                                         'cdfeb fcadb cdfeb cdbaf') == '5353'

    def test_get_digit(self):
        assert day08.get_digit('fc', self.dict) == '1'
        assert day08.get_digit('dcaeg', self.dict) == '2'
        assert day08.get_digit('dcfga', self.dict) == '3'
        assert day08.get_digit('dbcf', self.dict) == '4'
        assert day08.get_digit('gfdba', self.dict) == '5'
        assert day08.get_digit('gefdab', self.dict) == '6'
        assert day08.get_digit('cfa', self.dict) == '7'
        assert day08.get_digit('acfgedb', self.dict) == '8'
        assert day08.get_digit('bcdfga', self.dict) == '9'
        assert day08.get_digit('fegcab', self.dict) == '0'

    def test_dictionary_writer(self):
        correct_dict = {'0': 'cagedb', '1': 'ab', '2': 'gcdfa', '3': 'fbcad', '4': 'eafb',
                        '5': 'cdfbe', '6': 'cdfgeb', '7': 'dab', '8': 'acedgfb', '9': 'cefabd'}
        data = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
        assert day08.dictionary_writer(data) == correct_dict

    def test_part1(self):
        assert day08.part1('/../inputs/day08_test.txt') == 26
        assert day08.part1('/../inputs/day08_final.txt') == 554

    def test_part2(self):
        assert day08.part2('/../inputs/day08_test.txt') == 61229
        assert day08.part2('/../inputs/day08_final.txt') == 990964
            