from ..puzzles import day21
import pytest


@pytest.mark.skip
class TestDay21:
    def create_players(self):
        self.players = day21.create_players_from_input(['anything here is irrevelant: 2', 'nothing: 10'])

    def create_board(self, players=None):
        self.board = day21.Board(players)

    def test_create_players_from_input(self):
        self.create_players()
        assert len(self.players) == 2
        for player in self.players:
            assert type(player) == day21.Player
        assert self.players[0] != self.players[1]

    def test_roll_a_dice(self):
        die = day21.Die()
        assert die.current_number == 0
        assert die.roll() == 1
        assert die.current_number == 1

    def test_die_is_wrapped(self):
        die = day21.Die()
        die.current_number = 99
        assert die.roll() == 100
        assert die.roll() == 1

    def test_get_players(self):
        self.create_board()
        assert self.board.get_players() == []

        self.create_players()
        self.create_board(self.players)
        for player in self.players:
            assert player in self.board.get_players()

    def test_place_player_on_board_during_creation(self):
        self.create_players()
        self.create_board(self.players)
        assert self.board.localise_player(self.players[0]) == 2
        assert self.board.localise_player(self.players[1]) == 10

    def test_players_can_be_at_the_same_spot(self):
        self.create_players()
        self.create_board(self.players)
        self.board.move_player_on_board(self.players[1], 2)
        assert self.board.localise_player(self.players[0]) == self.board.localise_player(self.players[1])

    def test_player_points_after_move(self):
        self.create_players()
        self.create_board(self.players)
        self.board.move_player_on_board(self.players[1], 2)
        assert self.players[1].score == 2
        self.board.move_player_on_board(self.players[1], 12)
        assert self.players[1].score == 6

    def test_move_player_on_board(self):
        self.create_players()
        self.create_board(self.players)
        assert self.board.localise_player(self.players[1]) == self.players[1].starting_position
        assert self.board.move_player_on_board(self.players[1], 2) == 2
        assert self.board.move_player_on_board(self.players[1], 2) == 4
        assert self.board.localise_player(self.players[1]) == 4

    def test_board_fields(self):
        assert day21.Board().board == {1: [], 2: [], 3: [], 4: [], 5: [],
                                       6: [], 7: [], 8: [], 9: [], 10: []}
        self.create_players()
        self.create_board(self.players)
        assert self.board.board == {1: [], 2: [self.players[0]], 3: [], 4: [], 5: [],
                              6: [], 7: [], 8: [], 9: [], 10: [self.players[1]]}

    def test_part1(self):
        assert day21.part1('/../inputs/day21_test.txt') == 739785
        assert day21.part1('/../inputs/day21_final.txt') == 518418

    def test_part2(self):
        assert not day21.part2('/../inputs/day21_test.txt')
    #     assert not day21.part2('/../inputs/day21_final.txt')
            