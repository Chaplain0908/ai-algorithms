'''
    Target: do not know which action is better, so learn which action can bering the highest reward(the best action) asap
    Background - K-Armed Bandit:
        we have a K-armed Bandit(k actions), every time we pull, we will get a reward
        the reward is fixed distributed, but we do not know at the beginning
        every term, we can only choose to pull An arm
        and the time of terms is limited
        we need to: maximize our total reward
    How :
        we balance exploration and exploitation
        exploration: try different actions and collect the information
        exploitation: choose the current best action and get the higher reward
    Algorithms Process:
        ε-Greedy - probability ε to explor, 1-ε to exploit
        UCB1 - balance explor and exploit
        Thompson Sampling - record the probability of get reward for all arms, and choose the highest to pull
'''
import numpy as np
import math

class Bandit:
    def __init__(self, k):
        self.k = k # number of arms
        self.reward_means = np.random.uniform(low=-1.0, high=1.0, size=k) # average reward for each arm, generate randomly
        self.best_arm = np.argmax(self.reward_means)  # find the best arm with the highest reward
        # return the index of max val

    # player pull an arm, and return the arm's reward
    def pull(self, arm):
        arm_mean = self.reward_means[arm]
        get_reward = np.random.normal(loc=arm_mean, scale=1.0)
        return get_reward

    def get_best_arm(self):
        return self.best_arm

    def get_means(self):
        return self.reward_means

    # reset the reward for experiment
    def reset(self):
        self.reward_means = np.random.uniform(low=-1.0, high=1.0, size=self.k)
        self.best_arm = np.argmax(self.reward_means)
        return self.reward_means

def epsilon_greedy(bandit, epsilon=0.1, steps=1000):
    '''

    :param bandit: a bandit object, with k arms
    :param epsilon:  probability of exploration, generally 0.1 or 0.001
    :param steps:  total times of try
    :return: estimate_reward - list[], estimated average reward of each arm
             action_counts - list[], times of arms been chosen
             reward_per_step - list[], reward of every turn
             optimal_action_counts - list[], whether every step choose the best arm (evaluate the effect of algorithm)
    '''
    estimate_reward = [0 for _ in range(bandit.k)]
    action_counts = [0 for _ in range(bandit.k)]
    reward_per_step = []
    optimal_action_counts = []

    for step in range(steps):
        # choose arm
        if np.random.rand() < epsilon:
            select_arm = np.random.choice(bandit.k) # explor randomly
        else:
            select_arm = np.argmax(estimate_reward) # greedy

        # pull bandit to get the reward
        reward = bandit.pull(select_arm)
        reward_per_step.append(reward)

        # whether the select arm is now the best arm
        if select_arm == bandit.get_best_arm():
            optimal_action_counts.append(True)
        else:
            optimal_action_counts.append(False)

        # update the times of action in the select_arm value
        action_counts[select_arm] += 1
        # update the estimate_reward of select_arm (incremental average)
        estimate_reward[select_arm] += (1 / action_counts[select_arm]) * (reward - estimate_reward[select_arm])

    return estimate_reward, action_counts, reward_per_step, optimal_action_counts

# balance explor and exploit
def UCB1(bandit, steps=1000):
    '''

    :param bandit: a bandit object, with k arms
    :param steps: total times of try
    :return: estimate_reward, action_counts, reward_per_step, optimal_action_counts
    '''
    estimate_reward = [0 for _ in range(bandit.k)]
    action_counts = [0 for _ in range(bandit.k)]
    reward_per_step = []
    optimal_action_counts = []

    # start, every arm pull once first
    for arm in range(bandit.k):

        # pull every arm to get reward
        reward = bandit.pull(arm)
        reward_per_step.append(reward)

        # update the times of action in the select_arm value
        action_counts[arm] += 1

        # update estimate_reward
        estimate_reward[arm] += (1 / action_counts[arm]) * (reward - estimate_reward[arm])

        # whether the select arm is now the best arm
        optimal_action_counts.append(arm == bandit.get_best_arm())

    # calculate the ucb value and update estimate_reward, action_counts, reward_per_step, optimal_action_counts
    for j in range(bandit.k, steps):
        # calculate the UCB value
        arm_ucb_value = []
        for arm in range(bandit.k):
            mean_reward = estimate_reward[arm]
            arm_count = action_counts[arm]
            step_index = j+1 # j starts from bandit.k, total step count is j+1
            ucb_value = mean_reward + math.sqrt(2*math.log(step_index)/arm_count)
            arm_ucb_value.append(ucb_value)

        # choose the arm with the highest UCB
        select_arm = np.argmax(arm_ucb_value)

        # pull that arm and get the reward
        reward = bandit.pull(select_arm)
        reward_per_step.append(reward)

        # update estimate_reward, action_counts, reward_per_step, optimal_action_counts
        action_counts[select_arm] += 1
        estimate_reward[select_arm] += (1 / action_counts[select_arm]) * (reward - estimate_reward[select_arm])
        optimal_action_counts.append(select_arm == bandit.get_best_arm())

    return estimate_reward, action_counts, reward_per_step, optimal_action_counts

# record the probability of get reward for all arms, and choose the highest to pull, based on Bayesian sampling
def thompson_sampling(bandit, steps=1000):
    '''

    variables:
        success - the time of every arm get success(high reward)
        failure - the time of every arm get failure
        reward_per_step - reward received in every step
        optimal_action_counts - whether every step choose the best arm (evaluate the effect of algorithm)
    :return: success, failure, reward_per_step, optimal_action_counts
    '''
    success = [1 for _ in range(bandit.k)]
    failure = [1 for _ in range(bandit.k)]
    reward_per_step = []
    optimal_action_counts = []

    for _ in range(steps):
        success_prob = []
        for arm in range(bandit.k):
            # use beta distribution to construct the probability of successful in every arm, from the successful times and failure times
            sample_value = np.random.beta(success[arm], failure[arm])
            success_prob.append(sample_value)
        best_arm = np.argmax(success_prob)

        # pull the best arm
        reward = bandit.pull(best_arm)

        # update the times of success and failure
        if reward > 0:
            success[best_arm] += 1
        else:
            failure[best_arm] += 1

        # update the rewards
        reward_per_step.append(reward)

        # update the optimal_action_counts
        optimal_action_counts.append(best_arm == bandit.get_best_arm())

    return success, failure, reward_per_step, optimal_action_counts













