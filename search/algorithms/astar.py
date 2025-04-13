import heapq

def astar(problem):
    '''
    A_star Search algorithm.

    Parameter: an object inherits from SearchProblem

    Return:
    - list of actions, from start to goal, eg.['Down', 'Right', 'Right']
    - cannot find solution, return empty list[]
    '''

    start_state = problem.get_start_state()

    frontier = []
    heapq.heappush(frontier, (0, 0, start_state, []))
    # (f(x)=g(x)+heuristic(x), g(x), position, action list)

    explored = set()

    while frontier:
        fx, gx, state, path = heapq.heappop(frontier)

        if problem.is_goal_state(state):
            return path

        if state in explored:
            continue

        explored.add(state)

        for successor, action, step_cost in problem.get_successors(state):
            if successor not in explored:
                gx_new = gx+step_cost
                hx_new = manhattan_distance(successor, problem.get_goal_state())
                fx_new = gx_new+hx_new
                heapq.heappush(frontier, (fx_new, gx_new, successor, path + [action]))


    return []

def manhattan_distance(x, y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])