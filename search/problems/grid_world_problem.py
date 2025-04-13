from .search_problem import SearchProblem

class GridWorldProblem(SearchProblem):
    def __init__(self, grid, start, goal, rewards=None, step_cost=1):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rewards = rewards if rewards else {}
        self.step_cost = step_cost
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
                    pos = (next_x, next_y)
                    next_rewards = self.rewards.get(pos, 0) # if there is no rewards, the rewards will be 0
                    next_cost = self.step_cost - next_rewards # reward reduce cost, penalty increase cost
                    successors.append(((next_x, next_y), actions, next_cost))
        return successors

    # total cost from start to end
    def get_cost_of_actions(self, actions):
        x, y = self.start
        total_cost = 0

        for action in actions:
            if action == 'Up':
                x -= 1
            elif action == 'Down':
                x += 1
            elif action == 'Left':
                y -= 1
            elif action == 'Right':
                y += 1
            if x < 0 or x > self.rows-1 or y < 0 or y > self.cols-1 or self.grid[x][y] == 1:
                return float('inf')
            cur_rewards = self.rewards.get((x, y), 0)
            cur_cost = self.step_cost - cur_rewards
            total_cost += cur_cost

        return total_cost



