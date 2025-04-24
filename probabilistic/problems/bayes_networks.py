'''
Sprinkler-Rain-WetGrass Network:
    Cloudy
    /    \
Rain   Sprinkler
   \     /
   WetGrass
   
Background description:
    we need to decide the wetgrass is caused by rain or by sprinkler
    the cloudy whether affect to whether it will rain or not, and also the sprinkler
    rain and sprinkler both decide the wetgrass 
'''
def get_rain_network():
    '''
    parent: list of parent node
    cpt: Conditional Probability Table(CPT), when given the parent node, the prob to take the current node
    :return: bayes_net
    '''
    bayes_net = {
        'Cloudy': {
            'parents': [],
            'prob': {
                True: 0.5,
                False: 0.5
            }
        },
        'Sprinkler': {
            'parents': ['Cloudy'],
            'prob': {
                (True,): {True: 0.1, False: 0.9},
                (False,): {True: 0.5, False: 0.5}
            }
        },
        'Rain': {
            'parents': ['Cloudy'],
            'prob': {
                (True,): {True: 0.8, False: 0.2},
                (False,): {True: 0.2, False: 0.8}
            }
        },
        'WetGrass': {
            'parents': ['Sprinkler', 'Rain'],
            'prob': {
                (True, True): {True: 0.99, False: 0.01},
                (True, False): {True: 0.90, False: 0.10},
                (False, True): {True: 0.90, False: 0.10},
                (False, False): {True: 0.0, False: 1.0}
            }
        }
    }

    return bayes_net, ['Cloudy', 'Sprinkler', 'Rain', 'WetGrass']








