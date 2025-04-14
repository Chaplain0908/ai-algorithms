def constraint_fn(value1, value2):
    if value1 == value2:
        return False
    return True

def create_map_coloring_csp():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    colors = ['red', 'green', 'blue']

    domains = {}
    for var in variables:
        domains[var] = colors

    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    constraints = []
    for var in variables:
        for neighbor in neighbors[var]:
            constraints.append((var, neighbor, constraint_fn))

    return variables, domains, constraints