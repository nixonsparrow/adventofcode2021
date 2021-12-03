from ..puzzles import day01


class TestDay01:

    def test_sonar_sweep(self):
        assert day01.sonar_sweep([1, 3, 5, 5]) == 2
        assert day01.sonar_sweep([1, 1, 1, 1]) == 0
        assert day01.sonar_sweep([1, 3, 1, 3, 1]) == 2
        assert day01.sonar_sweep([5, 4, 3, 2, 1]) == 0

        assert day01.sonar_sweep([1, 3, 5, 5], wide=True) == 1
        assert day01.sonar_sweep([5, 4, 3, 2, 1], wide=True) == 0
        assert day01.sonar_sweep([1, 3, 1, 3, 1], wide=True) == 1
        assert day01.sonar_sweep([1, 2, 3, 4, 3, 4, 3], wide=True) == 3

    def test_part1(self):
        assert day01.part1('/../inputs/day01_test.txt') == 7
        assert day01.part1('/../inputs/day01_final.txt') == 1298

    def test_part2(self):
        assert day01.part2('/../inputs/day01_test.txt') == 5
        assert day01.part2('/../inputs/day01_final.txt') == 1248
