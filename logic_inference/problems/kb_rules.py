def kb_rules():
    """
    return a clauses list of CNF for test
    """
    return [
        ['¬A', 'B'],  # A → B
        ['¬B', 'C'],  # B → C
        ['A', 'D'],  # A ∨ D
        ['¬C', '¬D'],  # C → ¬D
        ['¬D', 'E'],  # D → E
        ['¬E']  # E must be false
    ]