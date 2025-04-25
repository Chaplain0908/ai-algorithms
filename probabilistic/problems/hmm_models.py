'''
Umbrella World:
    you cannot know the weather directly(hidden state), but you can get the weather information
    by state of umbrella bringing(observe evidence)
Definition of Umbrella World:
    Hidden States: real weather
        Rain
        No Rain
    Observations:
        Umbrella
        No Umbrella
'''

def get_umbrella_hmm():
    hmm = {
        'states': ['Rainy', 'Sunny'], # hidden
        'observations': ['Umbrella'], # observation
        'start_prob': {
            'Rainy': 0.5,
            'Sunny': 0.5
        },
        'trans_prob': { # P(hidden_t-1 | hidden_t)
            'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
            'Sunny': {'Rainy': 0.3, 'Sunny': 0.7}
        },
        'emission_prob': { # P(hidden_t | observation_t)
            'Rainy': {'Umbrella': 0.9, 'NoUmbrella': 0.1},
            'Sunny': {'Umbrella': 0.2, 'NoUmbrella': 0.8}
        }
    }
    return hmm