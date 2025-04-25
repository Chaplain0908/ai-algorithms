from probabilistic.algorithms.particle_filtering import particle_filtering
from probabilistic.problems.hmm_models import get_umbrella_hmm

hmm_model = get_umbrella_hmm()

observations = [
    'NoUmbrella', 'NoUmbrella', 'Umbrella', 'Umbrella', 'Umbrella',
    'NoUmbrella', 'Umbrella', 'NoUmbrella', 'NoUmbrella', 'Umbrella'
]

filtered_probs = particle_filtering(observation=observations, hmm=hmm_model)

for t, dist in enumerate(filtered_probs):
    print(f"Time {t + 1}:")
    for state, prob in dist.items():
        print(f"  {state}: {prob:.4f}")
    print()

from probabilistic.visualize.particle_distribution import plot_particle_filtered_probs
plot_particle_filtered_probs(filtered_probs)