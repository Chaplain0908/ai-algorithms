'''
DPLL (Davis–Putnam–Logemann–Loveland)
Target: Given CNF, it's SAT or UNSAT? Return a model (satisfying assignment)
Input: CNF
Output: True and Model / False and None

clause = l1 or l2 or l3 ... or ln
clauses = clause1 and clause2 and clause3 ... and clausen
'''
from copy import deepcopy

def dpll(clauses, assignment=None):
    """
    use DPLL to solve the CNF is SAT or UNSAT

    :param clauses: List[List[str]], gathering of clause, which contains literal
    :param assignment: Dict[str, bool], the value of current variable, do iteration and expand
    :return: (bool, assignment or None)
    """
    clauses, assignment = unit_propagate(clauses, assignment)
    if clauses is None:
        return None

    clauses, assignment = pure_literal_assign(clauses, assignment)

    if len(clauses) == 0:
        return assignment
    for clause in clauses:
        if len(clause) == 0:
            return None

    literal = choose_literal(clauses, assignment)
    if literal is None:
        return assignment

    # Try assigning True
    var = literal.strip('¬')
    for value in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        new_clauses = deepcopy(clauses)
        result = dpll(new_clauses, new_assignment)
        if result is not None:
            return result

    return None

def unit_propagate(clauses, assignment):
    """
    unite_propagate:
    if exist the clause with only one literal, then take this literal as true, ¬literal as false
    then traverse all the clause:
    if the clause include the unite_clause, then the whole clauses must be true, so this clause can be deleted
    if the clause include the ¬unite_clause, then the whole clause must be False, but we do not know except the ¬unite_clause, which causes UNSAT
        then we only delete the ¬unite_clause in the clause
    """
    if assignment is None:
        assignment = {}

    while True:
        unit_clause = None # fine the unit_clause in clauses, eg. clauses = [['¬A'], ['B', '¬C'], ['D']]
        for clause in clauses:
            if len(clause) == 1:
                unit_clause = clause[0]
                break

        if unit_clause is None: # there is no unit clause in clauses
            break

        # variable and bool value
        var = unit_clause.strip('¬') # if is ¬A, var = A
        value = None
        if unit_clause[0] == '¬':
            value = False
        else:
            value = True

        if var in assignment and assignment[var] != value:
            return None, None  # Conflict
        assignment[var] = value

        # update clauses
        new_clauses = []
        for clause in clauses:
            if unit_clause in clause: # this clause is SAT(True, because unit_clause is included), the whole clause can be deleted
                continue

            # has skip the clause including unit_clause, then only skip the clause including ¬unit_clause(negated_literal)
            # this clause is UNSAT, but must include a False literal, so we delete this False literal, to see whether the rest of literal can be SAT
            negated_literal = None
            if value:
                negated_literal = '¬'+var
            else:
                negated_literal = var

            if negated_literal in clause: # for clause in clauses, if negated_literal in clause, then delete
                new_clause = []
                for literal in clause:
                    if literal != negated_literal:
                        new_clause.append(literal)
                new_clauses.append(new_clause)
            else:
                new_clauses.append(clause)

        clauses = new_clauses

    return clauses, assignment


def pure_literal_assign(clauses, assignment):
    """
    pure_literal: in all clauses, if a variable is only True(eg.A), or only False(eg.¬A), then it is pure_literal
    Therefore, we can make this pure_literal as True(A), and delete the clause if it contains A
        or delete the literal in clause if it is ¬A
    """
    # find all the pure_literal
    literal_records = set()
    for clause in clauses:
        for literal in clause:
            var = literal.strip('¬')
            if var == literal:
                if '¬'+literal in literal_records:
                    literal_records.remove('¬'+literal)
                else:
                    literal_records.add(var)
            else:
                if var in literal_records:
                    literal_records.remove(var)
                else:
                    literal_records.add(literal)

    # make the value of the pure_literal
    for literal in literal_records:
        if literal.startswith('¬'):
            assignment[literal[1:]] = False
        else:
            assignment[literal] = True

    # delete clause including pure_literal
    new_clauses = []
    for clause in clauses:
        for literal in clause:
            if literal in literal_records:
                break
        else:
            new_clauses.append(clause)

    clauses = new_clauses

    return clauses, assignment

def choose_literal(clauses, assignment):
    """
    target: choose a literal without value and use it in branch
    """
    for clause in clauses:
        for literal in clause:
            var = literal.strip('¬')
            if var not in assignment:
                return literal
    return None

