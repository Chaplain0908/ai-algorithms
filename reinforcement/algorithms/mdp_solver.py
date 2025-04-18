'''
    MDP(Markov Decision Process) - build an agent to get the maximize long-term reward in an environment by doing actions
    Target:
        find a strategy(what actions should be taken in every state)
        makes the agent to get the max accumulated expected return from the start state
    Parts:
        S: state space
        A: action space
        T(s, a, s'): state transition function - given state s and action a, return the probability of transitioning to state s' from s
        R(s, a, s'): reward function - the immediate reward received when transitioning from state s to s' by taking action a
        γ (gamma): discount factor - a value between [0,1) that determines the present value of future rewards
    Algorithm process:
        Dynamic process:
            value iteration
            policy iteration
        Reinforcement learning:
            Q-learning
'''
from reinforcement.algorithms.policy_iteration import policy_iteration
from reinforcement.algorithms.value_iteration import value_iteration
from reinforcement.algorithms.q_learning import q_learning

def solve_mdp(env, method='value_iteration', **kwargs):
    """
    use different algorithm to solve mdp problem

    :param env: MDPEnv object
    :param method: algorithm name, can choose ['value_iteration', 'policy_iteration', 'q_learning']
    :param kwargs: parameter of specific algorithm
    :return: dict，including policy and state_values
    """

    if method == 'value_iteration':
        gamma = kwargs.get('gamma', 0.9)
        theta = kwargs.get('theta', 1e-5)
        state_values = value_iteration(env, gamma=gamma, theta=theta)

        # get policy from state_value
        policy = {}
        for state in env.get_all_accessible_states():
            if env.is_terminal(state):
                continue
            best_action = None
            best_q = float('-inf')
            for action in env.get_next_actions(state):
                trans = env.get_transition_probs_and_rewards(state, action)
                q = sum(p * (r + gamma * state_values.get(s_, 0.0)) for p, s_, r in trans)
                if q > best_q:
                    best_q = q
                    best_action = action
            policy[state] = best_action

        return {'policy': policy, 'state_values': state_values}

    elif method == 'policy_iteration':
        gamma = kwargs.get('gamma', 0.9)
        theta = kwargs.get('theta', 1e-5)
        policy, state_values = policy_iteration(env, gamma=gamma, theta=theta)
        return {'policy': policy, 'state_values': state_values}

    elif method == 'q_learning':
        alpha = kwargs.get('alpha', 0.1)
        gamma = kwargs.get('gamma', 0.9)
        epsilon = kwargs.get('epsilon', 0.1)
        episodes = kwargs.get('episodes', 500)
        policy, Q = q_learning(env, episodes=episodes, alpha=alpha, gamma=gamma, epsilon=epsilon)

        state_values = {}
        for state in policy:
            state_values[state] = max(Q[state].values()) if Q[state] else 0.0

        return {'policy': policy, 'state_values': state_values}

    else:
        raise ValueError(f"Unsupported method: {method}")





