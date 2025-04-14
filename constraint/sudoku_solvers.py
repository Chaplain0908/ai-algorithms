from constraint import csp_solver

def constraint_fn(value1, value2):
    if value1 == value2:
        return False
    return True

def create_sudoku_csp(grid):
    variables = []
    for i in range(9):
        for j in range(9):
            variables.append((i, j))

    domains = {}
    for var in variables:
        domains[var] = list(range(1, 10))

    constraints = []
    for i in range(len(variables)):
        for j in range(i+1, len(variables)):
            x1, y1 = variables[i]
            x2, y2 = variables[j]
            if x1 == x2 or y1 == y2 or (x1//3 == x2//3 and y1//3 == y2//3):
                value1 = domains[variables[i]]
                value2 = domains[variables[j]]
                constraints.append((variables[i], variables[j], constraint_fn))

    return variables, domains, constraints