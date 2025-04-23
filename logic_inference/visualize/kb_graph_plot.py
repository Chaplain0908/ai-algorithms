import networkx as nx
import matplotlib.pyplot as plt
from logic_inference.problems.kb_rules import kb_rules


def plot_kb_dependency_graph(clauses):
    """
    Visualize a knowledge base (KB) in CNF form as a dependency graph.

    Each literal (e.g., 'A', '¬B') becomes a node, and implications are shown as edges.
    For each clause [A, B, ¬C], it is interpreted as "A or B or ¬C",
    which we can transform to a loose implication graph, e.g., (¬A => B), etc.

    :param clauses: List[List[str]], CNF clauses where each clause is a list of literals
    """
    G = nx.DiGraph()

    for clause in clauses:
        # For clauses with more than one literal, assume some loose implication
        if len(clause) >= 2:
            for i in range(len(clause)):
                for j in range(len(clause)):
                    if i != j:
                        source = negate_literal(clause[i])  # if A in clause, then edge from ¬A
                        target = clause[j]                   # to B means ¬A => B
                        G.add_edge(source, target)
        elif len(clause) == 1:
            # Unit clause: single literal must be true
            G.add_edge("True", clause[0])

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, arrowsize=20)
    plt.title("Knowledge Base Dependency Graph")
    plt.show()


def negate_literal(literal):
    """
    Return the negation of a literal.
    If the input is 'A', return '¬A'; if input is '¬A', return 'A'.
    """
    if literal.startswith('¬'):
        return literal[1:]
    else:
        return '¬' + literal


if __name__ == "__main__":
    # Example test clauses
    example_kb = kb_rules()

    plot_kb_dependency_graph(example_kb)
