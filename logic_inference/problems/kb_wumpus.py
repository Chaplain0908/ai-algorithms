def kb_wumpus():
    """
    Return a clauses list of CNF for Wumpus World in 4x4 grid.
    Use propositional variables like W12 (Wumpus in (1,2)), B21 (Breeze in (2,1)), P33 (Pit in (3,3)), S34 (Stench in (3,4)), G22 (Gold in (2,2))
    """
    clauses = []

    # Stench rules: If there's a Wumpus in (x, y), then stench in adjacent squares
    # W23 → S13 ∧ S22 ∧ S24 ∧ S33 == ['¬W23', 'S13'], ['¬W23', 'S22'], ...
    clauses += [['¬W23', 'S13'], ['¬W23', 'S22'], ['¬W23', 'S24'], ['¬W23', 'S33']]

    # Breeze rules: If there's a pit, then breeze around
    clauses += [['¬P12', 'B11'], ['¬P12', 'B22'], ['¬P12', 'B13']]

    # If there is stench in (1,2), then Wumpus must be in one of its neighbors
    clauses += [['¬S12', 'W11', 'W22', 'W13']]

    # If breeze in (2,2), then pit must be in one of neighbors
    clauses += [['¬B22', 'P12', 'P21', 'P32', 'P23']]

    # One square can't have both pit and Wumpus
    clauses += [['¬P22', '¬W22']]

    # Add some facts (observations)
    clauses += [['S12'], ['B22'], ['¬B11']]  # Observed true/false

    return clauses
