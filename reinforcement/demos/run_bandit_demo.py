'''
Target:
    Compare the performance of three algorithms—ε-greedy, UCB1, and Thompson Sampling—in the Bandit problem
How:
    doing multiple experiments (multiple bandit instances) and take the average results
Output:
    Average reward per step (measures convergence speed)
    Proportion of selecting the optimal arm per step (measures accuracy)
'''

from reinforcement.algorithms.bandit_theory import Bandit, epsilon_greedy, UCB1, thompson_sampling
import matplotlib.pyplot as plt
import numpy as np

def bandit_compare():
    bandit_arms = 10
    steps = 1000
    runs = 2000 # experiment times

    avg_rewards = {
        'epsilon': np.zeros(steps),
        'ucb1': np.zeros(steps),
        'thompson': np.zeros(steps)
    }

    optimal_action_counts = {
        'epsilon': np.zeros(steps),
        'ucb1': np.zeros(steps),
        'thompson': np.zeros(steps)
    }

    for run in range(runs):
        bandit = Bandit(bandit_arms)

        _, _, rewards, opt = epsilon_greedy(bandit, epsilon=0.1, steps=steps)
        avg_rewards['epsilon'] += rewards
        optimal_action_counts['epsilon'] += opt

        _, _, rewards, opt = UCB1(bandit, steps=steps)
        avg_rewards['ucb1'] += rewards
        optimal_action_counts['ucb1'] += opt

        _, _, rewards, opt = thompson_sampling(bandit, steps=steps)
        avg_rewards['thompson'] += rewards
        optimal_action_counts['thompson'] += opt

    avg_rewards['epsilon'] /= runs
    optimal_action_counts['epsilon'] /= runs

    avg_rewards['ucb1'] /= runs
    optimal_action_counts['ucb1'] /= runs

    avg_rewards['thompson'] /= runs
    optimal_action_counts['thompson'] /= runs

    return avg_rewards, optimal_action_counts
