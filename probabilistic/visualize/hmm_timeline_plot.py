import matplotlib.pyplot as plt

def plot_hmm_filtered_probs(hmm, filtered_probs, title="HMM Filtering Probabilities"):
    states = hmm['states']
    time_steps = len(filtered_probs)

    for state in states:
        probs = [dist[state] for dist in filtered_probs]
        plt.plot(range(1, time_steps + 1), probs, marker='o', label=state)

    plt.xlabel("Time Step")
    plt.ylabel("Probability")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
