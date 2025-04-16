import numpy as np
from search.problems.grid_world_problem import GridWorldProblem
from search.algorithms.bfs import bfs
from search.algorithms.dfs import dfs
from search.algorithms.ucs import ucs
from search.algorithms.astar import astar
from search.visualize.draw_path import draw_path

# generate an accessible 20*20 map randomly
np.random.seed(42)
grid = np.random.choice([0, 1], size=(20, 20), p=[0.7, 0.3]) # 70% is accessible, 30% cannot get through
start = (0, 0)
goal = (19, 19)

# make sure the start and goal is accessible
grid[start] = 0
grid[goal] = 0

# reward definition
'''
rewards = {
    (1, 2): -2,   # pos: penalty or reward, penalty, the cost will increase
    (2, 2): +1    # reward, the cost will reduce
}
'''
# reward randomly pick
rewards = {}
num_rewards = 10
reward_positions = list(zip(
    np.random.randint(0, 20, size=num_rewards),
    np.random.randint(0, 20, size=num_rewards)
))

for pos in reward_positions:
    if pos == start or pos == goal:
        continue  # do not cover the start and the goal
    rewards[pos] = np.random.choice([-5, -3, -1, 1, 3, 5])  # penalty or reward

def test_algorithm(algorithm_fn, name):
    print(f"\nRunning {name} in grid world...")
    problem = GridWorldProblem(grid, start, goal)
    path = algorithm_fn(problem)
    print("Path length:", len(path))
    print("Path: ", path if len(path) <= 20 else path[:10] + ['...'])
    print("Total cost:", problem.get_cost_of_actions(path))

    draw_path(grid, path, start, goal, f"{name} result", False, None)

test_algorithm(bfs, "BFS")
test_algorithm(dfs, "DFS")
test_algorithm(astar, "A*")
test_algorithm(ucs, "UCS")
