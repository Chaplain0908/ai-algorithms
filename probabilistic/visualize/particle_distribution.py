import matplotlib.pyplot as plt
import numpy as np

def plot_particle_filtered_probs(filtered_probs, title="Particle Filtered Probabilities"):
    states = list(filtered_probs[0].keys())
    time_steps = len(filtered_probs)
    x = np.arange(time_steps)

    bar_width = 0.35
    for i, state in enumerate(states):
        y = [filtered_probs[t][state] for t in range(time_steps)]
        plt.bar(x + i * bar_width, y, width=bar_width, label=state)

    plt.xlabel("Time Step")
    plt.ylabel("Probability")
    plt.title(title)
    plt.xticks(x + bar_width / 2, [str(t + 1) for t in range(time_steps)])
    plt.legend()
    plt.tight_layout()
    plt.show()
