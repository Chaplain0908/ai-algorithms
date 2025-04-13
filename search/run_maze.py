import numpy as np
from search.problems.maze_problem import MazeProblem
from search.algorithms.bfs import bfs
from search.algorithms.dfs import dfs
from search.algorithms.astar import astar
from search.algorithms.ucs import ucs
from search.visualize.draw_path import draw_path

# generate an accessible 20*20 map randomly
np.random.seed(42)
grid = np.random.choice([0, 1], size=(20, 20), p=[0.7, 0.3]) # 70% is accessible, 30% cannot get through
start = (0, 0)
goal = (19, 19)

# make sure the start and goal is accessible
grid[start] = 0
grid[goal] = 0

def test_algorithm(algorithm_fn, name):
    print(f"\nRunning {name}...")
    problem = MazeProblem(grid, start, goal)
    path = algorithm_fn(problem)
    print("Path length:", len(path))
    print("Path: ", path if len(path) <= 20 else path[:10] + ['...'])
    draw_path(grid, path, start, goal, f"{name} result", False, None)


test_algorithm(bfs, "BFS")
test_algorithm(dfs, "DFS")
test_algorithm(ucs, "UCS")
test_algorithm(astar, "A*")





