from reinforcement.problems.tic_tac_toe_game import TicTacToeGame
from reinforcement.algorithms.mcts import mcts_decision

def run_tic_tac_toe_game(state, game):
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
        print("Draw!")

game = TicTacToeGame()
state = game.initial_state()
run_tic_tac_toe_game(state, game)









