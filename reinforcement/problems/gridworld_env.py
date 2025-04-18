import random
import numpy as np

class MDPEnv:
    def __init__(self, grid, start_state, goal_state, rewards, transition_probs):
        self.grid = grid # List[List[str]]
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start_state = start_state # Tuple[int, int], start position
        self.goal_states = goal_state # Set[Tuple[int,int]]
        self.rewards = rewards if rewards else {} # Dict[state, float], reward of some places
        self.actions = ['Up', 'Down', 'Left', 'Right'] # action can be chosen
        self.transition_probs = transition_probs
        # Dict[action, List[(action, prob)]], main action and probability of the next different direction action
        # eg. {'Up': [('Up', 0.8), ('Left', 0.1), ('Right', 0.1)]}

    def get_all_accessible_states(self):
        '''return all possible pos can be accessed'''
        all_states = set()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0: # accessible
                    all_states.add((i, j))

        return all_states

    # actions can be done cur, which will not lead to the inaccessible pos
    def get_next_actions(self, state):
        '''return action list'''
        all_actions = []
        for action in self.actions:
            x, y = state
            if action == 'Up':
                x -= 1
            elif action == 'Down':
                x += 1
            elif action == 'Left':
                y -= 1
            elif action == 'Right':
                y += 1
            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0:
                all_actions.append(action)

        return all_actions

    # in cur state and take the action, how much prob to transfer what states, and get how much reward
    def get_transition_probs_and_rewards(self, state, action):
        """
        return [(probability, next_state, reward)]
        """
        transition_probs_and_rewards = []

        next_probs = self.transition_probs[action]
        for next_action, prob in next_probs:
            x, y = state

            if next_action == 'Up':
                x -= 1
            elif next_action == 'Down':
                x += 1
            elif next_action == 'Left':
                y -= 1
            elif next_action == 'Right':
                y += 1

            if 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0:
                next_state = (x, y)
            else:
                next_state = state

            reward = self.rewards.get(next_state, 0)
            transition_probs_and_rewards.append((prob, next_state, reward))

        return transition_probs_and_rewards

    def is_terminal(self, state):
        return state in self.goal_states

    def reset(self):
        '''Q learning'''
        accessible_state = set()
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 0 and self.grid[i][j] not in self.goal_states:  # accessible
                    accessible_state.add((i, j))
        random_element = random.choice(list(accessible_state))
        return random_element # start_place

    def select_next_step(self, state, action):
        '''return next_state, reward, is_terminal'''

        transition_probs_and_rewards = self.get_transition_probs_and_rewards(state, action)
        probs = [prob for prob, _, _ in transition_probs_and_rewards]
        choices = [(next_state, reward) for _, next_state, reward in transition_probs_and_rewards]

        idx = np.random.choice(len(choices), p=probs)
        next_state, reward = choices[idx]
        is_terminal = self.is_terminal(next_state)

        return next_state, reward, is_terminal