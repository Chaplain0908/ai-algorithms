from .search_problem import SearchProblem
import numpy as np

class MazeProblem(SearchProblem):
    def __init__(self, grid, start, goal):
        self.grid = grid # numpy 2D array
        self.start = start # start point (x, y)
        self.goal = goal # goal point (x, y)
        self.rows, self.cols = grid.shape

    def get_start_state(self):
        return self.start

    def get_goal_state(self):
        return self.goal

    def is_goal_state(self, state):
        return state == self.goal

    def get_successors(self, state):
        x, y = state
        directions = [(-1, 0, 'Up'), (1, 0, 'Down'),
                      (0, -1, 'Left'), (0, 1, 'Right')]
        successors = []
        for dx, dy, actions in directions:
            next_x, next_y = x+dx, y+dy
            if 0 <= next_x < self.rows and 0 <= next_y < self.cols:
                if self.grid[next_x][next_y] == 0: # can access
                    successors.append(((next_x, next_y), actions, 1)) # cost is 1
        return successors

    def get_cost_of_actions(self, actions):
        return len(actions)
