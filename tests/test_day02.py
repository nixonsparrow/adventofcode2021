from ..puzzles import day02
import pytest            


class TestDay2:

    def test_command_executor_part1(self):
        submarine = day02.Submarine()

        submarine.execute_wrong('forward 5')
        assert submarine.horizontal_position == 5
        submarine.execute_wrong('down 5')
        assert submarine.depth == 5
        submarine.execute_wrong('forward 8')
        assert submarine.horizontal_position == 13
        submarine.execute_wrong('up 3')
        assert submarine.depth == 2

        with pytest.raises(EnvironmentError) as error:
            submarine.execute_wrong('up 3')
        assert str(error.value) == "Submarines don't fly"

    def test_command_executor_part2(self):
        submarine = day02.Submarine()

        submarine.execute('forward 5')
        assert submarine.horizontal_position == 5
        assert submarine.depth == 0
        submarine.execute('down 5')
        assert submarine.aim == 5
        submarine.execute('forward 8')
        assert submarine.horizontal_position == 13
        assert submarine.depth == 40
        submarine.execute('up 3')
        assert submarine.aim == 2
        submarine.execute('down 8')
        assert submarine.aim == 10
        submarine.execute('forward 2')
        assert submarine.horizontal_position == 15
        assert submarine.depth == 60

    def test_part1(self):
        assert day02.part1('/../inputs/day02_test.txt') == 150
        assert day02.part1('/../inputs/day02_final.txt') == 1868935

    def test_part2(self):
        assert day02.part2('/../inputs/day02_test.txt') == 900
        assert day02.part2('/../inputs/day02_final.txt') == 1965970888
            