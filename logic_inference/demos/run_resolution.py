from logic_inference.algorithms.resolution import pl_resolution
from logic_inference.problems.kb_rules import kb_rules
from logic_inference.problems.kb_wumpus import kb_wumpus

def run_resolution_demo():
    clauses = kb_rules()  # can switch to kb_wumpus()
    query = 'C'  # take an example to show whether the query is valid(True)

    result = pl_resolution(clauses, query)

    print("Resolution Result")
    print("-----------------")
    print("Knowledge Base:", clauses)
    print("Query:", query)
    if result:
        print(f"The knowledge base entails '{query}' (Provable)")
    else:
        print(f"The knowledge base does NOT entail '{query}'")

if __name__ == "__main__":
    run_resolution_demo()