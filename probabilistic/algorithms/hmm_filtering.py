'''
given a HMM model and observation, inference prob of hidden state in each time point
'''

# P(Xt | e1:t)
# Xt: hidden state in time t, is Rainy or Sunny
# et: observation in time t, is Umbrella or NoUmbrella
# target: alpha_t(hidden) = P(hidden_t | observations)

def forward_algorithm(hmm, observations):
    '''
    calculate alpha_t(hidden_t) = P(hidden_t|observations)
                      = P(observation_t|hidden_t)*sigma(alpha_t-1(hidden_t-1)*P(hidden_t|hidden_t-1))
    :param hmm: hmm models
    :param observations: ['Umbrella', 'Umbrella', 'NoUmbrella', 'Umbrella']
    :return: List[Dict[state, probability]]
    '''
    filtered_probs = []

    states = hmm['states']
    start_prob = hmm['start_prob']
    emission_prob = hmm['emission_prob']
    trans_prob = hmm['trans_prob']

    first_obs = observations[0]

    # initialize
    # alpha_t(hidden_t) = P(hidden_t | observations)*P(hidden_t)/P(observations)
    alpha = {}
    for state in states:
        prior = start_prob[state]
        likelihood = emission_prob[state][first_obs]
        alpha[state] = prior*likelihood

    total = sum(alpha.values())
    for state in alpha:
        alpha[state] /= total

    filtered_probs.append(alpha)

    for t in range(1, len(observations)):
        obs = observations[t]
        prev_alpha = filtered_probs[-1]  # alpha_{t-1}
        new_alpha = {}

        for curr_state in states:
            # Prediction: sum over all prev_state of alpha_{t-1}(hidden_t-1) * P(hidden_t | hidden_t-1)
            predicted = 0.0
            for prev_state in states:
                predicted += prev_alpha[prev_state] * trans_prob[prev_state][curr_state]

            # Update with emission probability: alpha_t(hidden_t) = P(obs_t | hidden_t) * predicted
            likelihood = emission_prob[curr_state][obs]
            new_alpha[curr_state] = likelihood * predicted

        # Normalize
        total = sum(new_alpha.values())
        for state in new_alpha:
            new_alpha[state] /= total

        filtered_probs.append(new_alpha)

    return filtered_probs  # List[Dict[state -> probability]]