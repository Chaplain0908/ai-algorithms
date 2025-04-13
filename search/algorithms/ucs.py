import heapq

def ucs(problem):
    '''
    UCS Search algorithm.

    Parameter: an object inherits from SearchProblem

    Return:
    - list of actions, from start to goal, eg.['Down', 'Right', 'Right']
    - cannot find solution, return empty list[]
    '''

    start_state = problem.get_start_state()

    frontier = []
    heapq.heappush(frontier, (0, start_state, [])) # (g(x), position, action list)

    explored = set()

    while frontier:
        gx, state, path = heapq.heappop(frontier)

        if problem.is_goal_state(state):
            return path

        if state in explored:
            continue

        explored.add(state)

        for successor, action, step_cost in problem.get_successors(state):
            if successor not in explored:
                gx_new = gx+step_cost
                heapq.heappush(frontier, (gx_new, successor, path + [action]))


    return []