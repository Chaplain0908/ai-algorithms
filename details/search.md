# Search
In this part, we mainly focus on search algorithms, and I separate them into two categories — classical and adversarial:

- Classical Search:
  - Planning and search algorithms for deterministic, fully observable, and static environments.
  - Includes BFS (Breadth-First Search), DFS (Depth-First Search), UCS (Uniform Cost Search), and A*.

- Adversarial Search:
  - Planning and search algorithms for multi-agent environments, where the agent must find the optimal strategy assuming the opponent always chooses its best move.
  - Includes Minimax and Alpha-Beta Pruning (an optimization of Minimax).

## Search Subsections

- [Classical Search](#classical-search)
  - [Problem (Classical)](#problem-classical)
    - [Maze Problem](#maze-problem)
    - [Grid World Problem](#grid-world-problem)
    - [Eight Puzzle Problem](#eight-puzzle-problem)
  - [Algorithm (Classical)](#algorithm-classical)
    - [BFS (Breadth-First Search)](#bfsbreadth-first-search)
    - [DFS (Depth-First Search)](#dfs-depth-first-search)
    - [UCS (Uniform Cost Search)](#ucs-uniform-cost-search)
    - [A* (A Star Search)](#a-a-star-search)
  - [Results (Classical)](#results-classical)
    - [Maze Problem Result](#maze-problem)
    - [Grid World Problem Result](#grid-world-problem)
    - [Eight Puzzle Problem Result](#eight-puzzle-problem)

- [Adversarial Search](#adversarial-search)
  - [Problem (Adversarial)](#problem-adversarial)
    - [Tic-Tac-Toe Game](#tic-tac-toe-game)
  - [Algorithm (Adversarial)](#algorithm-adversarial)
    - [MinMax](#minmax)
    - [AlphaBeta Pruning (an optimization of Minimax)](#alphabeta-pruning-an-optimization-of-minimax)
  - [Results (Adversarial)](#results-adversarial)

  
## Classical Search
### Problem (Classical)
#### Maze Problem
- Definition: Given a standard 2D maze problem, consisting of a grid containing 0 or 1, where 0 means accessible and 1 means an obstacle. The start and goal positions are specified.
- Target: Find the shortest path from the start to the goal, moving only in four directions (up, down, left, right). Obstacles cannot be crossed.
- Evaluation Standard: Each movement costs 1, and the solution must find the shortest possible path.

#### Grid World Problem
- Definition: Similar to the standard 2D maze problem, but supports a more complex environment, such as:
  - Each state (position) can have rewards or punishments.
  - The step cost can be increased or decreased depending on the rewards or punishments.
- Target: Under the conditions of rewards and punishments, move from the start position to the goal position while achieving the lowest total cost.
- Evaluation Standard: By considering both the rewards and the path size, the goal is to find a path with minimal total cost.

#### Eight Puzzle Problem
- Definition: Given a 3×3 sliding puzzle that contains numbers from 1 to 8 and a blank space (represented by 0), with the state expressed as a 9-tuple.
- Target: Slide the blank space to exchange with adjacent numbers, and transform the initial state into the goal state, ensuring that the numbers are arranged in the specified order.
- Evaluation Standard: Count the number of slides as the cost, and the objective is to reach the goal state with the minimal number of slides.

### Algorithm (Classical)
#### BFS(Breadth-First Search)
- Propose: A typical graph or tree traversal algorithm. It can be used to find the shortest path from the start to the goal position, 
        or to determine whether a node is accessible.

- Input & Output:
  - Input: A graph or tree, a start position, a goal position
  - Output: The shortest path from the start to the goal position (if it exists)
  
- Idea: BFS uses a queue to traverse graph nodes layer by layer. 
       It starts from the start node and expands all reachable nodes level by level, until the goal node is found.
       (Since BFS explores nodes by layers, it can always find the shortest path.)

- Algorithm Step:
    ```
    Initialize a queue, enqueue the starting node, and mark it as visited.

    While the queue is not empty:
        a. Dequeue the front element as the current node.
        b. If the current node is the target node, return the path.
        c. Else, enqueue all unvisited neighboring nodes and mark them as visited.

    If the queue becomes empty without finding the target, return failure.
  ```

#### DFS (Depth-First Search)
- Propose: A typical graph traversal algorithm that explores as deep as possible before backtracking. 
          Can be used to check if a goal is reachable, but doesn't guarantee shortest path.

- Input & Output:
  - Input: A graph or tree, a start position, a goal position 
  - Output: A path from start to goal (if exists)

- Idea: DFS uses a stack to explore nodes. 
        It goes as deep as possible along each branch before backtracking. 
        It may find a solution quickly but does not ensure it's the shortest one.

- Algorithm Step:
  ```
  Initialize a stack, push the starting node, and mark it as visited.

  While the stack is not empty:
      a. Pop the top element as the current node.
      b. If the current node is the target, return the path.
      c. Else, push all unvisited neighboring nodes into the stack.
  
  If the stack becomes empty without finding the target, return failure.
  ```
  
#### UCS (Uniform Cost Search)
- Propose: A graph search algorithm used to find the lowest-cost path from start to goal, considering step costs. 
        Guarantees the optimal solution.

- Input & Output:
  - Input: A weighted graph, a start position, a goal position 
  - Output: The path from start to goal with the least total cost

- Idea: UCS uses a priority queue (min-heap), always expanding the node with the lowest cumulative cost (g(x)). 
       It's essentially a special case of A* with no heuristic.

- Algorithm Step:
  ```
  Initialize a priority queue with (0, start), and set visited to empty.

  While the queue is not empty:
      a. Pop the node with the lowest cost.
      b. If it is the goal, return the path.
      c. Else, add all unvisited successors with their new cost and enqueue.
  
  If the queue is empty without reaching the goal, return failure.
  ```
  
#### A* (A Star Search)
- Propose: An informed search algorithm that combines UCS's cost-so-far with a heuristic to guide the search more efficiently. 
          Returns optimal path if the heuristic is admissible.

- Input & Output:
  - Input: A weighted graph, a start and goal position, and a heuristic function 
  - Output: The path from start to goal with minimal estimated total cost

- Idea: A* uses a priority queue to expand nodes with the lowest estimated total cost f(x) = g(x) + h(x), 
      where g(x) is the actual cost and h(x) is the heuristic (here we use Manhattan distance).

- Algorithm Step:
  ```
  Initialize a priority queue with (f(start), g(start), start), and visited set.
  
  While the queue is not empty:
      a. Pop the node with the lowest f(x).
      b. If it is the goal, return the path.
      c. Else, for each successor:
          - Calculate new g(x), h(x), and f(x)
          - Push into queue if not visited
  
  If the queue is empty without reaching the goal, return failure.
  ```

### Results (Classical)
#### Maze Problem
<table>
    <tr>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/maze_problem/BFS.png" alt="BFS" style="width:100%"></td>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/maze_problem/DFS.png" alt="DFS" style="width:100%"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/maze_problem/UCS.png" alt="UCS" style="width:100%"></td>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/maze_problem/A_star.png" alt="A*" style="width:100%"></td>
    </tr>
</table>

#### Grid World Problem
<table>
    <tr>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/grid_world_problem/BFS.png" alt="UCS" style="width:100%"></td>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/grid_world_problem/DFS.png" alt="DFS" style="width:100%"></td>
    </tr>
    <tr>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/grid_world_problem/UCS.png" alt="UCS" style="width:100%"></td>
        <td><img src="https://github.com/Chaplain0908/ai-algorithms/raw/main/details/visualize_result/search/grid_world_problem/A_star.png" alt="A*" style="width:100%"></td>
    </tr>
</table>

#### Eight Puzzle Problem
```
Start state: (1, 8, 4, 5, 6, 0, 3, 7, 2)

Running BFS...
Path length: 17
Path:  ['Right', 'Right', 'Up', 'Up', 'Right', 'Down', 'Down', 'Left', 
       'Up', 'Right', 'Up', 'Left', 'Down', 'Left', 'Left', 'Down', 'Down']

Running UCS...
Path length: 17
Path:  ['Right', 'Right', 'Up', 'Up', 'Right', 'Down', 'Down', 'Left', 
       'Up', 'Right', 'Up', 'Left', 'Down', 'Left', 'Left', 'Down', 'Down']

Running A*...
Path length: 17
Path:  ['Right', 'Right', 'Up', 'Up', 'Right', 'Down', 'Down', 'Left', 
       'Up', 'Right', 'Up', 'Left', 'Down', 'Left', 'Left', 'Down', 'Down']
```
---

## Adversarial Search
### Problem (Adversarial)
#### Tic-Tac-Toe Game
- Definition: A classic two-player turn-based game played on a 3×3 board. 
            Players take turns placing their symbol (X for the first player, O for the second player) into empty cells. 
            The board is represented as a 3×3 list of characters.
- Target: Each player aims to place three of their own symbols in a horizontal, vertical, or diagonal line. 
         The agent (AI) must plan its moves under the assumption that the opponent will also choose their best possible actions.
- Evaluation Standard: A successful strategy should follow:
  - Maximize the chance of winning (three in a row)
  - Minimize the chance of losing by blocking the opponent
  - Lead to a draw if a win is not possible
  - In adversarial search, the agent’s goal is to maximize its own utility (+1 for win, 0 for draw, -1 for loss) under the assumption of perfect play from the opponent
- Required Interfaces:
    ```
    initial_state(): Initialize and return the initial board state.
    get_player(state): Determine whose turn it is based on the current board state.
    successors(state): Given the current board state, generate all possible next actions and their resulting new states.
    is_terminal(state): Determine whether the current state is a terminal state (win, loss, or draw).
    utility(state, player): Evaluate the current state for the given player, and return a corresponding score: +1 for a win, 0 for a draw, and -1 for a loss.
    is_win(state): Check whether there is a winner in the current state.
    display(state): Print the current board state for visualization.
    ```

### Algorithm (Adversarial)
#### MinMax
- Purpose:
  - In two-player adversarial games, assume the opponent always plays optimally, 
    and choose the action that maximizes your own utility while minimizing the opponent’s utility.
  - This algorithm is to plan your optimal choice, in order you get the best result(highest score). Although the opponent is also get the best result.
- Input & Output:
  - Input: Current game states(state), and the game object (game, including successor, is_terminal ect. The details have been showed in required interfaces of Tic-Tac-Toe Game).
  - Output: The optimal action (action) from the current state.
- Idea:
  - Do recursion to simulate the game tree, evaluating all possible actions for both the player (MAX layer) and the opponent (MIN layer).
  - At MAX layers, choose the action with the highest utility; at MIN layers, choose the one with the lowest utility.
  - Search until reaching a terminal state (win, loss, or draw), and return the corresponding utility (+1, 0, or -1).
- Algorithm Step:
  ```pseudocode
    def minimax_decision(state, game):
    if state is terminal:
        return utility of state
    best_score = -∞
    best_action = None
    for each (action, next_state) in successors(state):
        score = min_value(next_state, game)
        if score > best_score:
            best_score = score
            best_action = action
    return best_action
    
    def max_value(state, game):
        if state is terminal:
            return utility of state
        v = -∞
        for each (action, next_state) in successors(state):
            v = max(v, min_value(next_state, game))
        return v
        
    def min_value(state, game):
        if state is terminal:
            return utility of state
        v = +∞
        for each (action, next_state) in successors(state):
            v = min(v, max_value(next_state, game))
        return v
  ```

#### AlphaBeta Pruning (an optimization of Minimax)
- Purpose: Based on Minimax, Alpha-Beta Pruning reduces the number of nodes evaluated by pruning unnecessary branches during the search, 
          while still guaranteeing the correct decision.
- Input & Output:
  - Input: Current game state (state), the game object (game), 
          and two parameters: Alpha (the best value that MAX can guarantee) and Beta (the best value that MIN can guarantee).
  - Output: The optimal action (action) from the current state.
- Idea:
  - Same recursive structure as Minimax, but maintains two bounds:
    - Alpha: the best score MAX can guarantee so far.
    - Beta: the best score MIN can guarantee so far.
  - During search:
    - At MAX nodes, if a value ≥ Beta is found, prune (no need to explore further).
    - At MIN nodes, if a value ≤ Alpha is found, prune.
  - This avoids expanding branches that cannot possibly influence the final decision.
- Algorithm Step:
```pseudocode
    def alphabeta_decision(state, game):
        if state is terminal:
            return utility of state
        best_score = -∞
        best_action = None
        alpha = -∞
        beta = +∞
        for each (action, next_state) in successors(state):
            score = min_value(next_state, game, alpha, beta)
            if score > best_score:
                best_score = score
                best_action = action
        return best_action
    
    def max_value(state, game, alpha, beta):
        if state is terminal:
            return utility of state
        v = -∞
        for each (action, next_state) in successors(state):
            v = max(v, min_value(next_state, game, alpha, beta))
            if v >= beta:
                return v  // prune
            alpha = max(alpha, v)
        return v
    
    def min_value(state, game, alpha, beta):
        if state is terminal:
            return utility of state
        v = +∞
        for each (action, next_state) in successors(state):
            v = min(v, max_value(next_state, game, alpha, beta))
            if v <= alpha:
                return v  // prune
            beta = min(beta, v)
        return v
```

### Results (Adversarial)
<table>
<tr>
<th>MinMax</th>
<th>AlphaBeta Pruning</th>
</tr>
<tr>
<td>

```
  |   |
--+---+--
  |   |
--+---+--
  |   |
Current player: MAX
AI chooses: (0, 0)

X |   |  
--+---+--
  |   |  
--+---+--
  |   |  
Current player: MIN
AI chooses: (1, 1)

X |   |
--+---+--
  | O |
--+---+--
  |   |
Current player: MAX
AI chooses: (0, 1)

X | X |
--+---+--
  | O |
--+---+--
  |   |
Current player: MIN
AI chooses: (0, 2)

X | X | O
--+---+--
  | O |
--+---+--
  |   |
Current player: MAX
AI chooses: (2, 0)

X | X | O
--+---+--
  | O |
--+---+--
X |   |
Current player: MIN
AI chooses: (1, 0)

X | X | O
--+---+--
O | O |
--+---+--
X |   |
Current player: MAX
AI chooses: (1, 2)

X | X | O
--+---+--
O | O | X
--+---+--
X |   |
Current player: MIN
AI chooses: (2, 1)

X | X | O
--+---+--
O | O | X
--+---+--
X | O |
Current player: MAX
AI chooses: (2, 2)

Final State:
X | X | O
--+---+--
O | O | X
--+---+--
X | O | X
Draw!
```

</td> <td>

```
  |   |  
--+---+--
  |   |  
--+---+--
  |   |  
Current player: MAX
AI chooses: (0, 0)

X |   |  
--+---+--
  |   |  
--+---+--
  |   |  
Current player: MIN
AI chooses: (1, 1)

X |   |
--+---+--
  | O |
--+---+--
  |   |
Current player: MAX
AI chooses: (0, 1)

X | X |
--+---+--
  | O |
--+---+--
  |   |
Current player: MIN
AI chooses: (0, 2)

X | X | O
--+---+--
  | O |
--+---+--
  |   |
Current player: MAX
AI chooses: (2, 0)

X | X | O
--+---+--
  | O |
--+---+--
X |   |
Current player: MIN
AI chooses: (1, 0)

X | X | O
--+---+--
O | O |
--+---+--
X |   |
Current player: MAX
AI chooses: (1, 2)

X | X | O
--+---+--
O | O | X
--+---+--
X |   |
Current player: MIN
AI chooses: (2, 1)

X | X | O
--+---+--
O | O | X
--+---+--
X | O |
Current player: MAX
AI chooses: (2, 2)

Final State:
X | X | O
--+---+--
O | O | X
--+---+--
X | O | X
Draw!
```

</td> 
</tr> 
</table>