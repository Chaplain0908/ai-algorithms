class GridWorldMDP:
    def __init__(self, grid, terminals, walls, rewards, transition_prob=1.0):
        self.grid = grid
        self.terminals = terminals
        self.walls = walls
        self.rewards = rewards
        self.transition_prob = transition_prob

