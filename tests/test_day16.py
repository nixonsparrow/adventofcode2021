from ..puzzles import day16
import pytest


@pytest.mark.skip
class TestDay16:
    test_dicts = [{'sequence': '110100101111111000101000', 'hexadecimal': 'D2FE28',
                   'id': 4, 'version': 6, 'length_type_id': None},
                  {'sequence': '00111000000000000110111101000101001010010001001000000000', 'hexadecimal': '38006F45291200',
                   'id': 6, 'version': 1, 'length_type_id': 0},
                  {'sequence': '11101110000000001101010000001100100000100011000001100000', 'hexadecimal': 'EE00D40C823060',
                   'id': 3, 'version': 7, 'length_type_id': 1}]

    def test_translate_into_binary(self):
        for test_dict in self.test_dicts:
            assert day16.translate_into_binary(test_dict['hexadecimal']) == test_dict['sequence']

    def test_get_id(self):
        for test_dict in self.test_dicts:
            assert day16.get_id(test_dict['sequence']) == test_dict['id']

    def test_get_version(self):
        for test_dict in self.test_dicts:
            assert day16.get_version(test_dict['sequence']) == test_dict['version']

    def test_get_length_type_id(self):
        with pytest.raises(AttributeError):     # with id version: 4 it's not possible to seek length type ID
            day16.get_length_type_id(self.test_dicts[0]['sequence'])

        for test_dict in self.test_dicts[1:]:
            assert day16.get_length_type_id(test_dict['sequence']) == test_dict['length_type_id']

    def test_get_bin(self):
        assert day16.get_bin(0) == '0000'
        assert day16.get_bin(5) == '0101'
        assert day16.get_bin('F') == '1111'

    def test_read_literal_value(self):
        assert day16.read_literal_values('10111') == ('0111', False)
        assert day16.read_literal_values('11110') == ('1110', False)
        assert day16.read_literal_values('00101') == ('0101', True)

    # def test_compute(self):
    #     assert day16.compute(self.test_dicts[0]['sequence']) == 6
    #     assert day16.compute(self.test_dicts[1]['sequence']) == 9
    #     assert day16.compute(self.test_dicts[2]['sequence']) == 14

    # def test_part1(self):
    #     results = [16, 12, 23, 31]
    #     for nr in range(4):
    #         assert day16.part1(f'/../inputs/day16_test{nr + 1}.txt') == results[nr]
    #     assert not day16.part1('/../inputs/day16_final.txt')

    # def test_get_packets(self):
    #     sequence = day16.translate_into_binary('8A004A801A8002F478')
    #     print('test_get_packets', sequence)
    #     v = day16.compute(sequence)
    #     print('test_get_packets', v)
    #     assert 0

# 
#     def test_part2(self):
#         assert not day16.part2('/../inputs/day16_test1.txt')
#         assert not day16.part2('/../inputs/day16_final.txt')
            