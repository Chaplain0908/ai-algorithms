'''
class Game:
    def get_player(state) → "MAX" or "MIN"
    def is_terminal(state) → bool
    def utility(state, player) → float      #  +1 / -1 / 0
    def successors(state) → List[(action, new_state)]
'''

'''
For stage of MCTS(Monte Carlo tree search):
    1. Selection: 
        start in root, choose child node by UCB1, until the node that not fully expanded
    2. Expansion:
        choose an action that have never tried from the cur_node(not fully expanded), and expand a new node based on the chosen action
    3. Simulation:
        start in new expand node, randomly simulate the game until the terminal, get the reward
    4. Backpropagation
        propagate the reward from the bottom to root, update the visit time and simulation reword along the way
'''

import math
import random

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action # what the action to get the cur_node from its parent's node
        self.children = []
        self.visits = 0 # not visited
        self.total_reward = 0.0
        self.untried_actions = None # initial as None

    def is_fully_expanded(self, game):
        """
        have tried the all successors from game.successors(state)?
        which means all the child actions have been extended
        """
        if self.untried_actions is None:
            self.untried_actions = [action for action, _ in game.successors(self.state)]
        return len(self.untried_actions) == 0

    def best_child(self, c_param=1):
        """
        choose the best_child by using UCB1 algorithm
        """
        best_score = float('-inf')
        best_child = None
        for child in self.children:
            if child.visits == 0:
                continue

            # UCB1 algorithm
            exploitation = child.total_reward / child.visits
            exploration = math.sqrt(math.log(self.visits) / child.visits)
            score = exploitation + c_param*exploration
            if score > best_score:
                best_child = child
                best_score = score
        return best_child

    def expand(self, game):
        """
        from untried_actions randomly pick new_action, and use it and game.successor to get the new_state, and get a new_child_node
        """
        # choose a new node from untried
        if self.untried_actions is None:
            self.untried_actions = [action for action, _ in game.successors(self.state)]
        new_action = random.choice(self.untried_actions)
        self.untried_actions.remove(new_action)

        # find new_state to the new_action
        for action, new_state in game.successors(self.state):
            if new_action == action:
                new_child_node = Node(state=new_state, parent=self, action=new_action)
                self.children.append(new_child_node)
                return new_child_node

    def update(self, reward):
        """
        update visit time and simulated reward
        """
        self.visits += 1
        self.total_reward += reward

# find leaf node
def tree_policy(node, game): # Expansion
    '''
    when not terminal:
        if node fully expanded -> go down to find the best child;
            not fully expanded -> expand
    if terminal:
        return node
    '''
    while not game.is_terminal(node.state):
        if node.is_fully_expanded(game):
            node = node.best_child()
        else:
            node = node.expand(game)

    return node

# get the reward of leaf node
def default_policy(state, game): # Simulation
    player = game.get_player(state)
    cur_state = state # current position
    while not game.is_terminal(state):
        action, new_state = random.choice(game.successors(cur_state))
        cur_state = new_state

    return game.utility(cur_state, player)

# take the leaf node reward propagate to the root node, and update the visit time and rewards along the way
def backup(node, reward): # Backpropagation
    while node is not None:
        node.update(reward)
        node = node.parent

'''
    given state and game, simulate n times,
    start from root, and choose the action of node with largest visits
'''
def mcts_decision(state, game, iter_limit=1000): # return action
    root = Node(state, None, None)

    while iter_limit:
        node = root
        leaf_node = tree_policy(node, game)
        reward = default_policy(leaf_node.state, game)
        backup(leaf_node, reward)
        iter_limit -= 1

    visit_time = float('-inf')
    action = None
    for child in root.children:
        if child.visits > visit_time:
            visit_time = child.visits
            action = child.action

    return action