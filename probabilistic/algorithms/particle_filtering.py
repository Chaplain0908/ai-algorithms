import numpy as np
from collections import Counter

def sampling_particles(num_particles, prob, states):
    particle_list = np.random.choice(states, size=num_particles, p=prob)
    return particle_list

def particle_filtering(observation, hmm, N=100):
    # get hidden state
    states = hmm['states']

    # get prob of hidden state
    initial_prob = []
    for state in states:
        initial_prob.append(hmm['start_prob'][state])

    # do initial sampling
    particle_state = sampling_particles(N, initial_prob, states)

    # recording P(X_t | e_1:t) for every particle
    estimated = []

    # iterate obs in every time point
    for obs in observation:
        # particle weight for cur_state P(obs_t | particle_state)
        weights = []
        for state in particle_state:
            weights.append(hmm['emission_prob'][state][obs])

        # normalize
        total = sum(weights)
        for i in range(len(weights)):
            weights[i] = weights[i] / total

        # resampling
        particle_state = sampling_particles(num_particles=N, prob=weights, states=particle_state)

        # get next time state by trans_prob
        next_states = []
        for cur_state in particle_state:
            trans_probs = hmm['trans_prob'][cur_state]
            prob = []
            for state in states:
                prob.append(trans_probs[state])
            next_state = np.random.choice(states, p=prob)  # get next state by prob
            next_states.append(next_state)  # save new state

        particle_state = next_states  # update particle state as next state

        # statistics the current particle state to estimate the state distribution
        count = Counter(particle_state)

        norm = sum(count.values()) # normalize
        filtered = {}
        for state in states:
            filtered[state] = count[state] / norm

        estimated.append(filtered)

    return estimated # List[Dict[state -> probability]]










