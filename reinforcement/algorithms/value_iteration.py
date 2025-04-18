def calculate_q_value(transition_prob_and_reward, gamma, state_values):
    '''
    calculate the Q value of given state and action

    :param transition_prob_and_reward: (prob, next_state, reward)
    :param gamma: discount factor
    :param state_values: state_values[s'] shows the value of V(s') in state s
    :return: Q(s, a)
    '''
    q_value = 0.0
    # for all next_states s
    for prob, next_state, reward in transition_prob_and_reward:
        # Bellman Expectation
        q_value += prob * ( reward + gamma * state_values[next_state])
    return q_value

# do value iteration for env, find out the best state value V(s) in every actions
def value_iteration(env, gamma=0.9, theta=1e-5):
    state_space = env.get_all_accessible_states()
    state_values = {}
    # state_values: start from current state, take all the best action in the future, how much reward can get?
    for state in state_space:
        state_values[state] = 0.0

    while True:
        delta = 0.0 # max value change for state_value of each state to determinate whether convergence
        for state in state_space:
            if env.is_terminal(state):
                continue

            '''
            q_val: in cur pos take next_action, transfer to all possible next pos
                    every transfer has its own prob and reward
                    q_val is their average weight result
            '''
            q_values = []
            next_actions = env.get_next_actions(state)
            for next_action in next_actions:
                transition_prob_and_reward = env.get_transition_probs_and_rewards(state, next_action)
                q = calculate_q_value(transition_prob_and_reward, gamma, state_values)
                q_values.append(q)

            max_q = max(q_values) # ge the max q_value of total reward when in cur pos
            delta = max(delta, abs(max_q-state_values[state]))
            state_values[state] = max_q

        if delta < theta:
            break

    return state_values