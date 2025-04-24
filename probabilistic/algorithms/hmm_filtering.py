'''
given a HMM model and observation, inference prob of hidden state in each time point
'''

# P(Xt | e1:t)
# Xt: hidden state in time t, is Rainy or Sunny
# et: observation in time t, is Umbrella or NoUmbrella
# target: alphat(x) = P(Xt=x | e1:t)

def forward_algorithm(hmm, observations):
    '''

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
    # alpha1(x) = P(X1=x | e1) = P(e1 | X1=x)*P(X1=x) / P(e1)
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
        prev_alpha = filtered_probs[-1]  # α_{t-1}
        new_alpha = {}

        for curr_state in states:
            # Prediction: sum over all prev_state of α_{t-1}(prev_state) * P(curr_state | prev_state)
            predicted = 0.0
            for prev_state in states:
                predicted += prev_alpha[prev_state] * trans_prob[prev_state][curr_state]

            # Update with emission probability: α_t(curr_state) = P(e_t | curr_state) * predicted
            likelihood = emission_prob[curr_state][obs]
            new_alpha[curr_state] = likelihood * predicted

        # Normalize
        total = sum(new_alpha.values())
        for state in new_alpha:
            new_alpha[state] /= total

        filtered_probs.append(new_alpha)

    return filtered_probs  # List[Dict[state -> probability]]