from ..puzzles import day03


class TestDay03:
    def test_read_gamma_rate(self):
        assert day03.read_gamma_rate(['101', '000', '101']) == '101'
        assert day03.read_gamma_rate(['000', '000', '111']) == '000'
        assert day03.read_gamma_rate(['101', '000', '101'], epsilon=True) == '010'
        assert day03.read_gamma_rate(['000', '000', '111'], epsilon=True) == '111'

    def test_calculators(self):
        assert day03.calculate_power_consumption('101', '010') == 10
        assert day03.calculate_power_consumption('1', '0') == 0

        assert day03.calculate_life_support_rating('101', '010') == 10
        assert day03.calculate_life_support_rating('1', '0') == 0

    def test_check_real_bit(self):
        assert day03.check_real_bit(['101', '000', '101'], position=0) == '1'
        assert day03.check_real_bit(['101', '000', '101'], position=1) == '0'
        assert day03.check_real_bit(['101', '000', '101'], position=2) == '1'

    def test_remove_wrong_numbers(self):
        assert day03.remove_wrong_numbers(['100', '010', '111'], 0) == ['100', '111']
        assert day03.remove_wrong_numbers(['100', '010', '111'], 1) == ['010', '111']
        assert day03.remove_wrong_numbers(['100', '010', '111'], 2) == ['100', '010']

        assert day03.remove_wrong_numbers(['100', '010', '111'], 0, co2=True) == ['010']
        assert day03.remove_wrong_numbers(['100', '010', '111'], 1, co2=True) == ['100']
        assert day03.remove_wrong_numbers(['100', '010', '111'], 2, co2=True) == ['111']

    def test_part1(self):
        assert day03.part1('/../inputs/day03_test.txt') == 198
        assert day03.part1('/../inputs/day03_final.txt') == 2261546

    def test_part2(self):
        assert day03.part2('/../inputs/day03_test.txt') == 230
        assert day03.part2('/../inputs/day03_final.txt') == 6775520
            