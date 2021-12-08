
if __name__ == '__main__':
    for day in range(9, 26):
        nr = day if len(str(day)) > 1 else f'0{day}'
        with open(f'test_day{nr}.py', 'w+') as x:
            x.write(f'''from ..puzzles import day{nr}
import pytest


# class TestDay{nr}:
# 
#     def test_part1(self):
#         assert not day{nr}.part1('/../inputs/day{nr}_test.txt')
#         assert not day{nr}.part1('/../inputs/day{nr}_final.txt')
# 
#     def test_part2(self):
#         assert not day{nr}.part2('/../inputs/day{nr}_test.txt')
#         assert not day{nr}.part2('/../inputs/day{nr}_final.txt')
            ''')

#
# if __name__ == '__main__':
#     for day in range(1, 26):
#         with open(f'test_day{day}.py', 'w+') as the_day:
#             the_day.write(f'from ..puzzles import day{day}\n'
#                           f'\n\nclass TestDay{day}:\n\n'
#                           f'{" "*4}def test_part1(self):\n{" "*8}assert 2 == 2\n\n'
#                           f'{" "*4}def test_part2(self):\n{" "*8}assert 2 == 2\n')
