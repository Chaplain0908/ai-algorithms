from copy import deepcopy
from reinforcement.algorithms.mcts import mcts_decision

class TicTacToeGame:
    def __init__(self, state=None):
        '''
        :param state: empty board, represent as List[List[str]]
        '''

        if state is None:
            state = [[' ' for _ in range(3)] for _ in range(3)]
        self.state = state

    # whose the people will do the next step
    def get_player(self, state):
        cnt_first = 0
        cnt_second = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == 'X':
                    cnt_first += 1
                if state[i][j] == 'O':
                    cnt_second += 1
        if cnt_first <= cnt_second:
            return "MAX"
        return "MIN"

    # action is the place where the next step
    # return List[(action, new_state)]
    def successors(self, state):
        possible_state = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == ' ':
                    player = self.get_player(state)
                    new_state = deepcopy(state)
                    if player == "MAX":
                        new_state[i][j] = 'X'
                    else:
                        new_state[i][j] = 'O'
                    possible_state.append(((i, j), new_state))
        return possible_state

    # check whether is the terminal
    def is_terminal(self, state):
        if not self.successors(state) or self.is_win(state):
            return True
        return False

    # if the people just place his chase and win, then is +1
    # for the people wait other place his chase, is loss, then is -1
    def utility(self, state, player):
        winner = self.is_win(state)
        if winner is None:
            return 0
        elif (winner == 'X' and player == 'MAX') or (winner == 'O' and player == 'MIN'):
            return 1
        else:
            return -1

    # find out who is the winner
    def is_win(self, state):
        # check the row
        for row in state:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # check the col
        for col in range(3):
            if state[0][col] == state[1][col] == state[2][col] != ' ':
                return state[0][col]

        # check the diagonal
        if state[0][0] == state[1][1] == state[2][2] != ' ':
            return state[0][0]

        if state[0][2] == state[1][1] == state[2][0] != ' ':
            return state[0][2]

        return None

    # display the board
    def display(self, state):
        for i, row in enumerate(state):
            print(" | ".join(row))
            if i < 2:
                print("--+---+--")

    # initialize the state
    def initial_state(self):
        return deepcopy(self.state)

'''def run_tic_tac_toe_game(state, action, game):
    # state[1][1] = 'X' # make X to start first
    # step = 1

    while not game.is_terminal(state):
        # print(f"\nStep {step}:")
        game.display(state)
        print("Current player:", game.get_player(state))

        action = mcts_decision(state, game)
        print("AI chooses:", action)

        # Apply action to generate new state
        for a, new_state in game.successors(state):
            if a == action:
                state = new_state
                break

        # step += 1

    print("\nFinal State:")
    game.display(state)
    winner = game.is_win(state)
    if winner:
        print("Winner:", winner)
    else:
        print("Draw!")'''
