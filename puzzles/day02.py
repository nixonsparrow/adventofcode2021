from .methods import txt_opener


class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal_position = 0
        self.aim = 0

    def read_command(self, command_verse):
        command = command_verse.split()[0]
        value = int(command_verse.split()[1])
        return command, value

    def execute_wrong(self, command_verse):         # part 1 method
        command, value = self.read_command(command_verse)

        if command == 'forward':
            self.horizontal_position += value
        elif command == 'down':
            self.depth += value
        elif command == 'up':
            if value > self.depth:
                raise EnvironmentError("Submarines don't fly")
            self.depth -= value

    def execute(self, command_verse):               # part 2 method
        command, value = self.read_command(command_verse)

        if command == 'forward':
            self.horizontal_position += value
            self.depth += value * self.aim
        elif command == 'down':
            self.aim += value
        elif command == 'up':
            self.aim -= value


def part1(input_file=''):
    final_input = txt_opener(input_file, '\n')
    yellow_submarine = Submarine()
    for command in final_input:
        yellow_submarine.execute_wrong(command)
    return yellow_submarine.depth * yellow_submarine.horizontal_position


def part2(input_file=''):
    final_input = txt_opener(input_file, '\n')
    yellow_submarine = Submarine()
    for command in final_input:
        yellow_submarine.execute(command)
    return yellow_submarine.depth * yellow_submarine.horizontal_position
            