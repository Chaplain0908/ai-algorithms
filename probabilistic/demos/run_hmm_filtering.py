from probabilistic.algorithms.hmm_filtering import forward_algorithm
from probabilistic.problems.hmm_models import get_umbrella_hmm

hmm_model = get_umbrella_hmm()

observations = [
    'NoUmbrella', 'NoUmbrella', 'Umbrella', 'Umbrella', 'Umbrella',
    'NoUmbrella', 'Umbrella', 'NoUmbrella', 'NoUmbrella', 'Umbrella'
]

filtered_probs = forward_algorithm(hmm_model, observations)

for t, dist in enumerate(filtered_probs):
    print(f"Time {t + 1}:")
    for state, prob in dist.items():
        print(f"  {state}: {prob:.4f}")
    print()

from probabilistic.visualize.hmm_timeline_plot import plot_hmm_filtered_probs
plot_hmm_filtered_probs(hmm_model, filtered_probs)