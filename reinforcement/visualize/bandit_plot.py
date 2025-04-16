import matplotlib.pyplot as plt
from reinforcement.demos.run_bandit_demo import bandit_compare

avg_rewards, optimal_action_counts = bandit_compare()

# draw
plt.figure(figsize=(12,5))

# average reward curve
plt.subplot(1, 2, 1)
plt.title("Average Reward")
plt.plot(avg_rewards['epsilon'], label='Epsilon-Greedy')
plt.plot(avg_rewards['ucb1'], label='UCB1')
plt.plot(avg_rewards['thompson'], label='Thompson Sampling')
plt.xlabel("Steps")
plt.ylabel("Average Reward")
plt.legend()

# proportion of choose best arm curve
plt.subplot(1, 2, 2)
plt.title("Optimal Arm Chosen %")
plt.plot(optimal_action_counts['epsilon'], label='Epsilon-Greedy')
plt.plot(optimal_action_counts['ucb1'], label='UCB1')
plt.plot(optimal_action_counts['thompson'], label='Thompson Sampling')
plt.xlabel("Steps")
plt.ylabel("Optimal Action %")
plt.legend()

plt.tight_layout()
plt.show()