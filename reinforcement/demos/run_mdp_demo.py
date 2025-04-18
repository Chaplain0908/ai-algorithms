from reinforcement.demos.run_value_iteration import visualize_value_iteration
from reinforcement.demos.run_policy_iteration import visualize_policy_iteration
from reinforcement.demos.run_q_learning import visualize_q_learning
from reinforcement.problems.gridworld_env import MDPEnv

grid = [
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 0]
]

rewards = {
    (0, 2): +1,
    (1, 2): -1
}

start_state = (2, 0)
goal_states = [(0, 2), (1, 2)]

transition_probs = {
    'Up': [('Up', 0.8), ('Left', 0.1), ('Right', 0.1)],
    'Down': [('Down', 0.8), ('Left', 0.1), ('Right', 0.1)],
    'Left': [('Left', 0.8), ('Up', 0.1), ('Down', 0.1)],
    'Right': [('Right', 0.8), ('Up', 0.1), ('Down', 0.1)],
}

env = MDPEnv(grid, start_state, goal_states, rewards, transition_probs)

print("This is Value Iteration:")
visualize_value_iteration(grid, rewards, start_state, goal_states, transition_probs, env)

print("This is Policy Iteration:")
visualize_policy_iteration(grid, rewards, start_state, goal_states, transition_probs, env)

print("This is Q Learning:")
visualize_q_learning(grid, rewards, start_state, goal_states, transition_probs, env)