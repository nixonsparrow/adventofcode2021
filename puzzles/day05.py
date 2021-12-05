from .methods import txt_opener
import numpy as np


class Map:
    def __init__(self, size=(10, 10)):
        self.array = np.zeros(size)

    def draw_line(self, xy1, xy2, no_diag=False):
        x1, y1, x2, y2 = tuple(map(int, xy1.split(','))) + tuple(map(int, xy2.split(',')))

        if y1 == y2 or x1 == x2:
            self.draw_straight(x1, y1, x2, y2)
        else:
            if not no_diag:
                self.draw_diagonal(x1, y1, x2, y2)

    def draw_diagonal(self, x1, y1, x2, y2):
        xs = list(range(x1, x2 + 1) if x1 < x2 else reversed(range(x2, x1 + 1)))
        ys = list(range(y1, y2 + 1) if y1 < y2 else reversed(range(y2, y1 + 1)))

        for i in range(len(xs)):
            self.array[ys[i]][xs[i]] += 1

    def draw_straight(self, x1, y1, x2, y2):
        x1, x2 = (x1, x2) if x1 <= x2 else (x2, x1)
        y1, y2 = (y1, y2) if y1 <= y2 else (y2, y1)

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                self.array[y][x] += 1

    def count_crossings(self):
        return sum([1 for x in range(0, len(self.array)) for y in range(0, len(self.array)) if self.array[y][x] > 1])


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    a_map = Map((1000, 1000))
    [a_map.draw_line(row.split(' -> ')[0], row.split(' -> ')[1], no_diag=True) for row in final_input]
    return a_map.count_crossings()


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    a_map = Map((1000, 1000))
    [a_map.draw_line(row.split(' -> ')[0], row.split(' -> ')[1]) for row in final_input]
    return a_map.count_crossings()
            