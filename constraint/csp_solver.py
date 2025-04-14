# check whether cur_val in cur_variable obey the constraints or not
# return true or false
def is_consistent(variable, value, assignment, constraints):
    for var1, var2, constraint_fn in constraints:
        if var1 in assignment and var2 == variable:
            if not constraint_fn(assignment[var1], value):
                return False
        elif var1 == variable and var2 in assignment:
            if not constraint_fn(value, assignment[var2]):
                return False
    return True

# select an unassigned variable that will be assigned next
# return variable
def select_unassigned_variable(variables, assignment):
    for var in variables:
        if var not in assignment:
            return var
    return None

# return all the possible values that the cur variable can be assigned
def order_domain_values(variable, domains):
    return domains[variable]

def backtracking_search(variables, domains, constraints, assignment=None):
    """
    general Backtracking Search
    parameter：
        - variables: list of variable names
        - domains: dict[var] -> list of possible values
        - constraints: list of (var1, var2, constraint_fn)
            - constraint_fn(value1, value2) -> true
        - assignment: dict[var] -> value
    return：
        - assignment or None
    """
    if assignment is None:
        assignment = {}

    # all the variables are assigned
    if len(assignment) == len(variables):
        return assignment # return assignment result

    # select an variable
    var = select_unassigned_variable(variables, assignment)

    for value in order_domain_values(var, domains):
        if is_consistent(var, value, assignment, constraints):
            assignment[var] = value
            result = backtracking_search(variables, domains, constraints, assignment)
            if result is not None:
                return result
            del assignment[var] # pruning

    return None



