from constraint import csp_solver

def constraint_fn(value1, value2):
    x1, y1 = value1
    x2, y2 = value2

    if y1 == y2 or abs(x1-x2) == abs(y1-y2):
        return False

    return True

def create_nqueens_csp(n=8):
    variables = [f"Q{i}" for i in range(n)]

    domains = {}
    for i, var in enumerate(variables):
        var_domain_list = []
        for j in range(n):
            var_domain_list.append((i, j))
        domains[var] = var_domain_list

    constraints = []
    for i in range(n):
        for j in range(i+1, n):
            constraints.append((variables[i], variables[j], constraint_fn))

    return variables, domains, constraints