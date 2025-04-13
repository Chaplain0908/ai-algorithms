def dfs(problem):
    """
    Depth-First Search algorithm.

    Parameters:
    - problem: an object inheriting from SearchProblem

    Returns:
    - list of actions (e.g., ['Down', 'Right'])
    - empty list if no solution found
    """

    start_state = problem.get_start_state()

    # stack stores: (cur_action, action_list to cur_action)
    frontier = []
    frontier.append((start_state, []))

    # record visited state
    explored = set()

    while frontier:
        state, path = frontier.pop()

        if problem.is_goal_state(state):
            return path

        if state in explored:
            continue

        explored.add(state)

        for successor, action, step_cost in problem.get_successors(state):
            if successor not in explored:
                frontier.append((successor, path+[action]))

    return []
