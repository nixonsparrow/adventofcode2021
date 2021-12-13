from .methods import txt_opener
from time import sleep


class Cave:
    def __init__(self, symbol):
        self.symbol = symbol
        self.big = True if symbol.isupper() else False
        self.connections = []

    def __str__(self):
        return f'Cave: {self.symbol}'


class Guide:
    def __init__(self):
        self.all_caves = []
        self.routes = []
        self.banned_caves = []




def get_cave(symbol, caves):
    return [cave for cave in caves if cave.symbol == symbol][0]


def cave_sensor(graph):
    caves = []
    for path in graph:
        symbols = path.split('-')
        [(caves.append(Cave(cave))) for cave in symbols if cave not in [c.symbol for c in caves]]
        cave_1, cave_2 = [cave for cave in caves if cave.symbol == symbols[0]], [cave for cave in caves if cave.symbol == symbols[1]]
        cave_1[0].connections.append(cave_2[0])
        cave_2[0].connections.append(cave_1[0])
    return caves


def find_all_ways(graph):
    ways = []
    dead_ends = []
    caves = cave_sensor(graph)
    start, end = [cave for cave in caves if cave.symbol == 'start'][0], [cave for cave in caves if cave.symbol == 'end'][0]

    route = [0]
    while True:
        caves_visited = [start]
        cave = start
        i = 0

        while cave != end:
            next_cave = cave.connections[i]
            if next_cave not in caves_visited or next_cave.big:     # Found new connection
                route.append(i)
                caves_visited.append(next_cave)
                cave = cave.connections[i]
                i = 0
            else:                                                   # Check next connection
                i += 1



        if route not in ways:
            ways.append(route)

    # return caves


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    return find_all_ways(final_input)


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    return final_input
