from ..puzzles import day12
import pytest


@pytest.mark.skip
class TestDay12:
    def test_get_cave(self):
        cave1, cave2 = day12.Cave('ab'), day12.Cave('xyz')
        caves = [cave1, cave2]
        assert day12.get_cave('ab', caves) == cave1
        assert day12.get_cave('xyz', caves) == cave2

    def test_cave_sensor(self):
        assert len(day12.cave_sensor(['a-b'])) == 2
        assert len(day12.cave_sensor(['a-b', 'b-c'])) == 3
        assert len(day12.cave_sensor(['a-b', 'b-c', 'c-D'])) == 4

    def test_find_all_ways(self):
        assert day12.find_all_ways(['start-end']) == 1
        assert day12.find_all_ways(['start-a', 'a-end']) == 1
        # assert day12.find_all_ways(['start-a', 'start-end', 'b-end']) == 2
        # assert day12.find_all_ways(['start-A', 'A-b', 'A-end', 'b-end']) == 5

    # def test_part1(self):
    #     assert day12.part1('/../inputs/day12_test1.txt') == 1
    #     assert not day12.part1('/../inputs/day12_final.txt')

    # def test_part2(self):
    #     assert not day12.part2('/../inputs/day12_test1.txt')
    #     assert not day12.part2('/../inputs/day12_final.txt')
            