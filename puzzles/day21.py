from .methods import txt_opener


class Player:
    def __init__(self, starting_position, score=0, nr=None):
        self.starting_position = starting_position
        self.score = score

        self.nr = nr

    def add_score(self, points):
        self.score += points


class Die:
    def __init__(self, current_number=0, times_rolled=0):
        self.current_number = current_number
        self.times_rolled = times_rolled

    def increase_nr(self):
        self.current_number = self.current_number + 1 if self.current_number < 100 else 1

    def roll(self):
        self.increase_nr()
        self.times_rolled += 1
        return self.current_number


class Board:
    def __init__(self, players=None):
        self.board = {nr: [] for nr in range(1, 11)}
        if players:
            self.place_players(players)

        print('BOARD:', self.board)

    def place_players(self, players):
        for player in players:
            self.board[player.starting_position].append(player)

    def localise_player(self, player):
        for k, v in self.board.items():
            if player in v:
                return k

    def get_players(self):
        players = []
        [[players.append(player) for player in field] for field in self.board.values() if field]
        return players

    def move_player_on_board(self, player, steps):
        old_field = self.localise_player(player)
        print(player)
        print(steps, old_field)
        print(self.board)
        new_field = (steps + old_field) % 10
        new_field = new_field if new_field > 0 else 10
        self.board[old_field].remove(player)
        self.board[new_field].append(player)
        player.add_score(new_field)
        return new_field


def create_players_from_input(the_input):
    players = []
    for row in the_input:
        players.append(Player(int(row.split(':')[-1])))
    return players


def play_game(players, die, board, turn=1):

    while players[0].score < 1000 and players[1].score < 1000:
        turn = 0 if turn == 1 else 1
        rolls = die.roll(), die.roll(), die.roll()
        board.move_player_on_board(players[turn], sum(rolls))

    result = (players[0].score if players[0].score < players[1].score else players[1].score) * die.times_rolled
    return result


wins = {'p0': 0, 'p1': 0}


def play_quantum_game(players, board, turn=1):

    while players[0].score < 21 and players[1].score < 21:
        turn = 0 if turn == 1 else 1

        print('ANOTHER TURN:', players[turn], players[abs(turn - 1)], board, '\n', wins, 'p0.score:', players[0].score, 'p1.score:', players[1].score)

        for x in range(1, 4):
            board.move_player_on_board(players[turn], x)

            p0 = Player(board.localise_player(players[0]), players[0].score, nr=0)
            p1 = Player(board.localise_player(players[1]), players[1].score, nr=1)

            new_players = [p0, p1]

            play_quantum_game(new_players, Board(new_players), turn=turn)

    wins['p0'] += 1 if players[0].score >= 21 else 0
    wins['p1'] += 1 if players[1].score >= 21 else 0
    return wins


def part1(input_file):
    final_input = txt_opener(input_file, '\n')
    players = create_players_from_input(final_input)
    die, board = Die(), Board(players)

    result = play_game(players, die, board)

    return result


def part2(input_file):
    final_input = txt_opener(input_file, '\n')
    players = create_players_from_input(final_input)
    for x in range(2):
        players[x].nr = x

    play_quantum_game(players, Board(players))

    return wins
