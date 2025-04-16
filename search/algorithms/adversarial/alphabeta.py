'''
    now in max layer, it's successors are in min layer,
    so the player(max layer) should choose the max utility from the utility chosen by min layer
    which means, the children will filter it's utility first, and pick the min one to player
    the player will choose the utilities provided by children of it's max
'''
def max_val(state, game, alpha, beta, player):
    if game.is_terminal(state):
        return game.utility(state, player)

    val = float('-inf')
    for action, next_state in game.successors(state):
        val = max(val, min_val(next_state, game, alpha, beta, player))
        if val >= beta: # value too large for parent MIN to accept → prune
            return val
        alpha = max(alpha, val) # update alpha: best option MAX has found so far

    return val

def min_val(state, game, alpha, beta, player):
    if game.is_terminal(state):
        return game.utility(state, player)

    val = float('inf')
    for action, next_state in game.successors(state):
        val = min(val, max_val(next_state, game, alpha, beta, player))
        if val <= alpha: # value too small for parent MAX to accept → prune
            return val
        beta = min(beta, val) # update beta: best option MIN has found so far
    return val

def alphabeta_decision(state, game):
    '''
    given the cur game state and game objects, return the optimal action
    :param state: current game state
    :param game: objects provides the game rules (must support is_terminal, utility, successor, player)
    :return: optimal action

    class Game:
        def successors(self, state) -> List[(action, new_state)]
        def is_terminal(self, state) -> bool
        def utility(self, state, player) -> float
        def get_player(self, state) -> "MAX" or "MIN"

    What's the different between minimax and alphabeta?
        Suppose I'm in MAX layer, comparing two MIN children.
        The first child returns value = 9, so best_score = 9, alpha = 9.
        Now I evaluate the second MIN child:
            its first successor returns 5 → so MIN ≤ 5
        Since MAX already has 9 and MIN will pick ≤ 5,
        MAX will never choose this MIN → prune this child.
    '''
    player = game.get_player(state) # now in max

    if game.is_terminal(state):
        return game.utility(state, player)

    # choose the action and make the next state is optimal
    best_score = float('-inf')
    best_action = None
    alpha = float('-inf') # max knows the minimal optimal choice (from parent max)
    beta = float('inf') # min knows the maximal optimal choice (from parent min)
    for action, next_state in game.successors(state):
        score = min_val(next_state, game, alpha, beta, player) # I am in max, successor in min, successor will give me the min score, I should pick the max one among them
        if score > best_score:
            best_score = score
            best_action = action

    return best_action