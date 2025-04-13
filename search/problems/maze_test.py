import numpy as np
from .maze_problem import MazeProblem

grid = np.array([
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 0]
])

start = (0, 0)
goal = (2, 2)

problem = MazeProblem(grid, start, goal)

print("start:", problem.get_start_state())
print("whether is goal:", problem.is_goal_state((2, 2)))
print("accessible actions staring (0, 0):", problem.get_successors((0, 0)))