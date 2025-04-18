import random
from collections import defaultdict
import numpy as np

def q_learning(env, episodes, alpha, gamma, epsilon):
    '''

    get the optimal policy by interacting with env and learning an optimal action value
    :param env:
    :param episodes:
    :param alpha: learning rate, control how big or small the updates impact to the old q_value
    :param gamma: discount factor
    :param epsilon: determine the exploration(random) or greedy
    :return: optimal policy
    '''

    # initialize Q
    # Q[state][action] = value, do action in state, which get value pf Q
    Q = defaultdict(lambda: defaultdict(float))
    state_space = env.get_all_accessible_states()
    for state in state_space:
        actions = env.get_next_actions(state)
        for action in actions:
            Q[state][action] = 0.0

    # episode loop
    # by exploring and exploiting to update Q_value of each pair of action and state
    while episodes:
        state = env.reset() # get start pos
        is_terminal = False

        while not is_terminal:
            actions = env.get_next_actions(state)
            if np.random.rand() < epsilon:
                select_action = random.choice(actions)
            else:
                select_action = max(Q[state], key=Q[state].get)

            next_state, reward,  is_terminal =  env.select_next_step(state, select_action)
            Q[state][select_action] = Q[state][select_action] + alpha * (reward + gamma * max(Q[next_state].values()) - Q[state][select_action])
            state = next_state

        episodes -= 1

    # get the optimal policy from the trained Q_table
    policy = {}
    state_space = env.get_all_accessible_states()
    for state in state_space:
        if env.is_terminal(state):
            continue

        if not Q[state]:
            continue

        best_action = None
        best_value = float('-inf')
        for action, value in Q[state].items():
            if value > best_value:
                best_value = value
                best_action = action

        policy[state] = best_action

    return policy, Q











