import numpy as np
import random
from search.problems.eight_puzzle import EightPuzzleProblem
from search.algorithms.bfs import bfs
from search.algorithms.dfs import dfs
from search.algorithms.astar import astar
from search.algorithms.ucs import ucs
from search.visualize.draw_path import draw_path

# generate an accessible 20*20 map randomly
np.random.seed(42)
start_state = tuple(random.sample(range(9), 9))

def is_solvable(state):
    inv_count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inv_count += 1
    return inv_count % 2 == 0

# make sure the start_state is solvable
while True:
    start_state = tuple(random.sample(range(9), 9))
    if is_solvable(start_state):
        break

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
print(start_state)

def test_algorithm(algorithm_fn, name):
    print(f"\nRunning {name}...")
    problem = EightPuzzleProblem(start_state, goal_state)
    path = algorithm_fn(problem)
    print("Path length:", len(path))
    print("Path: ", path if len(path) <= 20 else path[:10] + ['...'])


test_algorithm(bfs, "BFS")
test_algorithm(ucs, "UCS")
test_algorithm(astar, "A*")





