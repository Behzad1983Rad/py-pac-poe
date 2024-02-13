class PyPacPoe:
    def __init__(self):
        self.state = {
            'score': {'X': 0, 'O': 0, 'T': 0},
            'num_wins': 0,
            'winner': None,
            'board': {
                'a1': None, 'b1': None, 'c1': None,
                'a2': None, 'b2': None, 'c2': None,
                'a3': None, 'b3': None, 'c3': None
            },
            'turn': 'X'
        }

    def start(self):
        print("----------------------")
        print("Let's play Py-Pac-Poe!")
        print("----------------------\n\n")
        self.state['num_wins'] = int(input("How many wins to play to? "))
        self.play_game()

    def play_game(self):
        self.init_game()
        while not self.state['winner']:
            self.print_board()
            move = self.get_move()
            self.state['board'][move] = self.state['turn']
            self.state['turn'] = 'O' if self.state['turn'] == 'X' else 'X'
            self.state['winner'] = self.get_winner()
        self.handle_winner()

    def init_game(self):
        self.state['board'] = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }
        self.state['turn'] = 'X'
        self.state['winner'] = None

    def print_board(self):
        b = self.state['board']
        print(
            """
                A   B   C
            1)  {} | {} | {} 
                ----------
            2)  {} | {} | {}
                ----------
            3)  {} | {} | {}
            """.format(
                str(b['a1'] or ' '), str(b['b1'] or ' '), str(b['c1'] or ' '),
                str(b['a2'] or ' '), str(b['b2'] or ' '), str(b['c2'] or ' '),
                str(b['a3'] or ' '), str(b['b3'] or ' '), str(b['c3'] or ' ')
            )
        )

    def get_move(self):
        while True:
            move = input(f"Player {self.state['turn']}'s Move (example B2): ").lower()
            if move in self.state['board'] and not self.state['board'][move]:
                return move
            else:
                print("Bogus move! Try again...\n")

    def get_winner(self):
        b = self.state['board']
        if b['a1'] and (b['a1'] == b['b1'] == b['c1']): return b['a1']
        if b['a2'] and (b['a2'] == b['b2'] == b['c2']): return b['a2']
        if b['a3'] and (b['a3'] == b['b3'] == b['c3']): return b['a3']
        if b['a1'] and (b['a1'] == b['a2'] == b['a3']): return b['a1']
        if b['b1'] and (b['b1'] == b['b2'] == b['b3']): return b['b1']
        if b['c1'] and (b['c1'] == b['c2'] == b['c3']): return b['c1']
        if b['a1'] and (b['a1'] == b['b2'] == b['c3']): return b['a1']
        if b['c1'] and (b['c1'] == b['b2'] == b['a3']): return b['c1']
        return None if None in b.values() else 'T'

    def handle_winner(self):
        self.print_board()
        if self.state['winner'] == 'T':
            print("Another tie!")
        else:
            print("Player", self.state['winner'], "wins the game!\n")
        self.state['score'][self.state['winner']] += 1
        print(f"SCORE:\nPlayer X: {self.state['score']['X']}  Player O: {self.state['score']['O']}  Ties: {self.state['score']['T']}\n")
        if self.state['score']['X'] == self.state['num_wins'] or self.state['score']['O'] == self.state['num_wins']:
            print(f"\nCongrats to player {self.state['winner']} for winning {self.state['num_wins']} game{'s' if self.state['num_wins'] > 1 else ''}!\n")
        else:
            self.play_game()

game = PyPacPoe()
game.start()
