"""
Target:
Test three algorithms: forward_search_bfs, forward_search_dfs, and forward_search_astar
Print the obtained path (action sequence) for each search method

Core Components:
- Define a gridworld-like planning problem (initial_state, goal_state, actions)
- Execute each algorithm and output results
"""

from planning.algorithm.forward_search import forward_search
from planning.problems.strips_model import get_example_planning_problem
from planning.visualize.visualize_plan import visualize_plan

initial_state, goal_state, actions = get_example_planning_problem()

plan_bfs = forward_search(initial_state, goal_state, actions, 'bfs')
plan_dfs = forward_search(initial_state, goal_state, actions, 'dfs')
plan_astar = forward_search(initial_state, goal_state, actions, 'astar')

print("BFS Plan:", plan_bfs)
print("DFS Plan:", plan_dfs)
print("A* Plan:", plan_astar)

if plan_astar:
    visualize_plan(initial_state, plan_astar, actions)
else:
    print("No plan found using A*.")