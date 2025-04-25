import matplotlib.pyplot as plt
import networkx as nx

def plot_bayes_network(bayes_net, title="Bayes Network: Sprinkler-Rain-WetGrass"):
    G = nx.DiGraph()
    for node, data in bayes_net.items():
        for parent in data['parents']:
            G.add_edge(parent, node)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, arrows=True, node_color='lightblue', node_size=2000, font_size=12)
    plt.title(title)
    plt.tight_layout()
    plt.show()
