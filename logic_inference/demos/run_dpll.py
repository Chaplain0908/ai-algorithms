'''
problems: kb_rules, kb_wumpus
solution: dpll_sat
return: bool(SAT/UNSAT), assignment(value of variables)
'''

from logic_inference.algorithms.dpll_sat import dpll
from logic_inference.problems.kb_rules import kb_rules
from logic_inference.problems.kb_wumpus import kb_wumpus
from logic_inference.visualize.sat_tree_plot import plot_dpll_decision_tree

#clauses = kb_rules()
clauses = kb_wumpus()

result = dpll(clauses)

if result is not None:
    print("SAT")
    print("Assignment:")
    for var, val in sorted(result.items()):
        print(f"  {var} = {val}")

    example_tree = {
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

    plot_dpll_decision_tree(example_tree)
else:
    print("UNSAT")