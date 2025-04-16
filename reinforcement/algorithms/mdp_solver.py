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