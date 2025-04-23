'''
DPLL(solver): can this clauses can be SAT or UNSAT, if it can be SAT, how assign it's value
Resolution(proof): can the target conclusion be derived from the given facts

eg: there is a group of kb:
1. A ∨ B
2. ¬A ∨ C
3. ¬C
when input all the clauses, DPLL will tell:
    can these clauses be true together
Resolution will performance:
    given the premise, and tell it "I want to prove ¬B",
    it will try to inference whether ¬B valid (¬B is true) from these clauses

pl - Propositional Logic
'''

def pl_resolution(clauses, query):
    # whether the clause implicate query, Proof by Contradiction
    negate_query = negate_literal(query)
    clauses = list(clauses)  # copy, pretending modifying the original input
    clauses.append([negate_query])

    new_clauses = []

    while True:
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvents = pl_resolve(clauses[i], clauses[j])
                for clause in resolvents:
                    # If any resolution result is the empty clause,
                    # it shows a contradiction has been derived,
                    # and the solver returns SAT
                    if clause == []:
                        return True
                    if clause not in clauses and clause not in new_clauses:
                        new_clauses.append(clause)

        # If new contains no new clauses (i.e., all newly generated clauses already exist in clauses),
        # it indicates that no empty clause can be derived,
        # and the solver returns UNSAT
        if not new_clauses:
            return False

        clauses.extend(new_clauses)
        new_clauses.clear()

def negate_literal(literal):
    # if it's A, return ¬A; if it's ¬A, return A
    var = literal.strip('¬')
    if var == literal:
        return '¬'+literal
    else:
        return var

def pl_resolve(clause1, clause2):
    '''
    eg.clause1 = ['A', 'B'], clause2 = ['¬B', 'C']
       pl_resolve(clause1, clause2) ➜ [['A', 'C']]
    '''
    new_clause = []
    for i, literal1 in enumerate(clause1):
        for j, literal2 in enumerate(clause2):
            if literal1 == '¬' + literal2 or literal2 == '¬' + literal1:
                resolvent = [l for k, l in enumerate(clause1) if k != i] + \
                            [l for k, l in enumerate(clause2) if k != j]
                new_clause.append(resolvent)

    return new_clause


























