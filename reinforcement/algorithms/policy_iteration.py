import random


def bellman_equation(transition_prob_and_reward, gamma, state_values):
    q_value = 0.0
    # for all next_states s
    for prob, next_state, reward in transition_prob_and_reward:
        # Bellman Expectation
        q_value += prob * ( reward + gamma * state_values[next_state])
    return q_value

def policy_evaluation(policy, env, gamma, theta):
    '''
    strategy: action chosen to be taken
    give a strategy pi, evaluate all states values
    :param policy: dict[state] → action, cur strategy
    :param env: environment object
    :param gamma: discount factor
    :param theta: convergence, when change of state value < theta, stop
    :return: dict[state] → float, total reward/value of every states
    '''
    state_space = env.get_all_accessible_states()
    state_value = {}
    for state in state_space:
        state_value[state] = 0

    while True:
        delta = 0
        for state in state_space:
            if env.is_terminal(state):
                continue

            # action of cur strategy in state
            action = policy[state]
            transition_prob_and_reward = env.get_transition_probs_and_rewards(state, action)
            q_val = bellman_equation(transition_prob_and_reward, gamma, state_value)

            delta = max(delta, abs(q_val-state_value[state]))
            state_value[state] = q_val

        if delta <= theta:
            break

    return state_value

def policy_improvement(policy, state_values, env, gamma):
    '''
    use current state value to improve strategy
    :param state_values: state → V(s)
    :param env: environment object
    :param gamma: discount factor
    :return: new_policy：dict[state] → action, updated strategy
             is_policy_stable：bool, whether the strategy is optimal
    '''
    new_policy = {}
    state_space = env.get_all_accessible_states()

    for state in state_space:
        if env.is_terminal(state):
            new_policy[state] = None
            continue

        next_actions = env.get_next_actions(state)
        q_value = float('-inf')
        best_action = None

        for action in next_actions:
            transition_prob_and_reward = env.get_transition_probs_and_rewards(state, action)
            cur_q_value = bellman_equation(transition_prob_and_reward, gamma, state_values)
            if cur_q_value > q_value:
                q_value = cur_q_value
                best_action = action

        new_policy[state] = best_action

    return new_policy, new_policy == policy # if it is true, convergence

def policy_iteration(env, gamma=0.9, theta=1e-5):
    '''
    iterate strategy evaluation and improvement, until the strategy(police) is no longer change
    :return: policy: optimal strategy pi
             state_value: final state_value V(s)
    '''
    # policy initialize
    policy = {}
    state_space = env.get_all_accessible_states()
    for state in state_space:
        if env.is_terminal(state):
            continue
        policy[state] = random.choice(env.get_next_actions(state))

    # evaluation and improvement
    while True:
        state_values = policy_evaluation(policy, env, gamma, theta)
        new_policy, is_stable = policy_improvement(policy, state_values, env, gamma)

        if is_stable:
            break

        policy = new_policy

    return policy,  state_values