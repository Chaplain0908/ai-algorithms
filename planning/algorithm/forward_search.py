'''
forward search:
    beginning at the original state, doing available actions, create new state
    continue expanding until reach the goal state
It is similar to state-action space, actions are controlled by preconditions and effects
What are needed for forward search:
    state: use set to represent the cur world, like {At(A), Has(Banana)}
    action: with preconditions and effects
            Action: Move(x, y)
            Preconditions: At(x)
            Effects: ¬At(x), At(y)
    planning problem:
            original state: set()
            actions: available actions
            goal state: set()
'''
from collections import deque
import heapq

def forward_search(initial_state, goal_state, actions, method='bfs'):
    """
    Use forward search (BFS) to find a sequence of actions to reach the goal.

    :param initial_state: set of predicates representing the start
    :param goal_state: set of predicates that should all be satisfied
    :param actions: list of Action objects
    :return: List of actions (plan) if found, else None
    """
    if method == 'bfs':
        return forward_search_bfs(initial_state, goal_state, actions)
    elif method == 'dfs':
        return forward_search_dfs(initial_state, goal_state, actions)
    elif method == 'astar':
        return forward_search_astar(initial_state, goal_state, actions)
    else:
        raise ValueError("Unknown method")

def forward_search_bfs(initial_state, goal_state, actions):
    """
    Forward search using BFS
    """
    queue = deque()
    visited = set()

    # Start with (state, plan_so_far)
    queue.append((frozenset(initial_state), []))
    visited.add(frozenset(initial_state))

    while queue:
        current_state, plan = queue.popleft()

        # Goal check
        if goal_state.issubset(current_state):
            return plan

        for action in actions:
            if action.is_applicable(current_state):
                next_state = action.apply(current_state)
                frozen_next = frozenset(next_state)
                if frozen_next not in visited:
                    visited.add(frozen_next)
                    queue.append((frozen_next, plan + [action.name]))

    return None  # No plan found

def forward_search_dfs(initial_state, goal_state, actions):
    """
    Forward search using DFS
    """
    frontier = []
    visited = set()

    # Start with (state, plan_so_far)
    frontier.append((frozenset(initial_state), []))
    visited.add(frozenset(initial_state))

    while frontier:
        current_state, plan = frontier.pop()

        # Goal check
        if goal_state.issubset(current_state):
            return plan

        for action in actions:
            if action.is_applicable(current_state):
                next_state = action.apply(current_state)
                frozen_next = frozenset(next_state)
                if frozen_next not in visited:
                    visited.add(frozen_next)
                    frontier.append((frozen_next, plan + [action.name]))

    return None  # No plan found

def heuristic(state, goal_state):
    # simple admissible heuristic: how many goal facts are still unsatisfied
    return len(goal_state - state)

def forward_search_astar(initial_state, goal_state, actions):
    """
    Forward search using A*
    """
    frontier = []
    visited = set()

    # Start with (state, plan_so_far)
    heapq.heappush(frontier, (0, 0, frozenset(initial_state), []))
    visited.add(frozenset(initial_state))

    while frontier:
        fx, gx, current_state, plan = heapq.heappop(frontier)

        # Goal check
        if goal_state.issubset(current_state):
            return plan

        for action in actions:
            if action.is_applicable(current_state):
                next_state = action.apply(current_state)
                frozen_next = frozenset(next_state)
                if frozen_next not in visited:
                    visited.add(frozen_next)
                    gx_next = gx + 1
                    fx_next = gx_next + heuristic(next_state, goal_state)
                    heapq.heappush(frontier, (fx_next, gx_next, frozen_next, plan + [action.name]))

    return None  # No plan found

