import networkx as nx

def topological_sort(bayes_net):
    G = nx.DiGraph()
    for var, data in bayes_net.items():
        for parent in data['parents']:
            G.add_edge(parent, var)
    return list(nx.topological_sort(G))

def enumeration_ask(query_var, evidence, bayes_net):
    '''

    :param query_var: query variable, like rain
    :param evidence: what are given like {'Sprinkler': True, 'WetGrass': True}
    :param bayes_net: get_rain_network()
    :return: {True: prob1, False: prob2} to represent P(query_var=True | evidence) and P(query_var=False | evidence)
    '''

    result = {}

    # P(X=x | e)
    # = P(X=x, e)/P(e)
    # = P(X=x, e)/P(X=True, e)+P(X=False, e)
    for value in [True, False]:
        extended_evidence = evidence.copy()
        extended_evidence[query_var] = value # X=x
        all_vars = topological_sort(bayes_net) # make it more stable
        result[value] = enumerate_all(all_vars, extended_evidence, bayes_net) # P(X=x, e)

    total = sum(result.values()) # P(e)
    for val in result:
        result[val] /= total # P(X=x, e)/P(e)

    return result

# find the value in cpt
def cpt(var, evidence, bayes_net):
    parents = bayes_net[var]['parents']

    if not parents:
        return bayes_net[var]['prob']

    parent_val = []
    for parent in bayes_net[var]['parents']:
        if parent in evidence:
            parent_val.append(evidence[parent])
        else:
            raise ValueError(f"Missing value for parent variable '{parent}' in evidence.")

    return bayes_net[var]['prob'][tuple(parent_val)]

def enumerate_all(variables, evidence, bayes_net):
    # calculate: P(all variables in vars ∣ evidence)
    # P = P(V1 | parents(V1)) × P(V2 | parents(V2)) × ... × P(Vn | parents(Vn))
    if not variables:
        return 1.0

    first, rest = variables[0], variables[1:]

    # P(first=e,rest) = P(first=e ∣ parents)⋅P(rest)
    if first in evidence:
        prob = cpt(first, evidence, bayes_net)
        return prob[evidence[first]] * enumerate_all(rest, evidence, bayes_net)
    else:
        total = 0
        for val in [True, False]:
            extended_evidence = evidence.copy()
            extended_evidence[first] = val
            prob = cpt(first, extended_evidence, bayes_net)
            total += prob[val] * enumerate_all(rest, extended_evidence, bayes_net)
        return total