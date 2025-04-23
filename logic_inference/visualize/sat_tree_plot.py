import networkx as nx
import matplotlib.pyplot as plt

def plot_dpll_decision_tree(tree, title="DPLL Decision Tree"):
    """
    Visualize a simplified DPLL decision tree.

    :param tree: A dictionary-based binary tree representing variable decisions.
                 Format:
                 {
                    'A': {
                        True: {
                            'B': {
                                True: 'SAT',
                                False: 'UNSAT'
                            }
                        },
                        False: 'UNSAT'
                    }
                 }
    :param title: Title of the plot.
    """
    G = nx.DiGraph()
    pos = {}
    labels = {}

    def build_graph(node, parent=None, label=None, x=0, y=0, level=1):
        if isinstance(node, dict):
            var = list(node.keys())[0]
            center_x = x
            for i, branch in enumerate([True, False]):
                branch_x = x + (i - 0.5) * 2**(-level)
                child = node[var][branch]
                G.add_edge(f"{var}@{x},{y}", f"{branch}@{branch_x},{y-1}")
                labels[f"{var}@{x},{y}"] = var
                labels[f"{branch}@{branch_x},{y-1}"] = str(branch)
                pos[f"{var}@{x},{y}"] = (x, y)
                pos[f"{branch}@{branch_x},{y-1}"] = (branch_x, y-1)
                build_graph(child, f"{branch}@{branch_x},{y-1}", branch, branch_x, y-2, level+1)
        else:
            G.add_edge(parent, f"{node}@{x},{y}")
            labels[f"{node}@{x},{y}"] = node
            pos[f"{node}@{x},{y}"] = (x, y)

    build_graph(tree, x=0, y=0)

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=False, arrows=True, node_size=1500, node_color="lightblue")
    nx.draw_networkx_labels(G, pos, labels)
    plt.title(title)
    plt.axis('off')
    plt.show()
