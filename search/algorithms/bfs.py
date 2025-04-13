from collections import deque

def bfs(problem):
    '''
    Breadth-First Search algorithm.

    Parameter: an object inherits from SearchProblem

    Return:
    - list of actions, from start to goal, eg.['Down', 'Right', 'Right']
    - cannot find solution, return empty list[]
    '''

    start_state = problem.get_start_state()

    # queue stores: (cur_action, action_list to cur_action)
    frontier = deque()
    frontier.append((start_state, []))

    # record visited state
    explored = set()

    while frontier:
        state, path = frontier.popleft()

        if problem.is_goal_state(state):
            return path

        if state in explored:
            continue

        explored.add(state)

        for successor, action, step_cost in problem.get_successors(state):
            if successor not in explored:
                frontier.append((successor, path+[action]))

    return [] # do not find the goal