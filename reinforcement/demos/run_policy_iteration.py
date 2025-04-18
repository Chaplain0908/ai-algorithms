from reinforcement.algorithms.mdp_solver import solve_mdp
from reinforcement.visualize.policy_heatmap import plot_policy_and_values

def visualize_policy_iteration(grid, rewards, start_state, goal_states, transition_probs, env):
    # visualize
    import numpy as np
    def render_policy_and_values(grid, state_values, policy):
        arrow_map = {
            'Up': '↑',
            'Down': '↓',
            'Left': '←',
            'Right': '→'
        }

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            row_display = ""
            for j in range(cols):
                if grid[i][j] == 1:
                    cell = "#####"
                else:
                    pos = (i, j)
                    val = state_values.get(pos, 0.0)
                    act = policy.get(pos, ' ')
                    arrow = arrow_map.get(act, ' ')
                    cell = f"{val:.2f}{arrow}"
                row_display += f"{cell:<8}"
            print(row_display)

    result = solve_mdp(env, method='policy_iteration', gamma=0.9, theta=1e-5)
    policy = result['policy']
    state_values = result['state_values']

    render_policy_and_values(grid, state_values, policy)
    plot_policy_and_values(grid, policy, state_values, title="Policy Iteration Result")


