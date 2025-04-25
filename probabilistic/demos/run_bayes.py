from probabilistic.problems.bayes_networks import get_rain_network
from probabilistic.algorithms.bayes_inference import enumeration_ask

# if the Sprinkler is open and grass is wet, what the prob is rain?
evidence = {'Sprinkler': True, 'WetGrass': True}
query = 'Rain'

bayes_net, _ = get_rain_network()
result = enumeration_ask(query, evidence, bayes_net)

print(f"P({query}=True | evidence) = {result[True]:.4f}")
print(f"P({query}=False | evidence) = {result[False]:.4f}")

from probabilistic.visualize.bayes_graph_plot import plot_bayes_network
plot_bayes_network(bayes_net)