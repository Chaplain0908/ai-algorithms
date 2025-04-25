# Project Background

This project is an AI Algorithm Collection developed based on the CS520 course at Rutgers University, 
and inspired by the book Artificial Intelligence: A Modern Approach by Russell and Norvig.

All algorithms in this project are implemented entirely in Python, 
without relying on external libraries for core logic 
(except for the Machine Learning and Neural Network modules, which use PyTorch for model training and fine-tuning).

The aim of this project is to build a self-contained educational framework that supports 
and extends future research in AI planning, probabilistic reasoning, and neural learning.

# Project Structure

This project is composed of eight main modules:
Search, Constraint, Logic Inference, Planning, Probabilistic, Reinforcement, Machine Learning, and Neural Networks.

Each module generally includes the following components:

- Algorithms – Contains the core implementations of algorithms that can be applied to various problems.
- Problems – Provides classic environments or problem definitions where the algorithms are applied.
- Demos – Offers a unified interface to run the algorithms on the problems and obtain results.
- Visualize – Visualizes the behavior and outcomes of the algorithms for each problem to make the results more intuitive and interpretable.

In this README, I will introduce every algorithm and problem included in the project, covering the background of each problem, 
the goal of the corresponding algorithm, how the algorithm works, and the final results—often visualized to provide a clearer understanding of the solution process.

# Project Parts
## Search

In this part, we mainly focus on search algorithms, and I separate them into two categories — classical and adversarial:

- Classical Search:
  - Planning and search algorithms for deterministic, fully observable, and static environments.
  - Includes BFS (Breadth-First Search), DFS (Depth-First Search), UCS (Uniform Cost Search), and A*.

- Adversarial Search:
  - Planning and search algorithms for multi-agent environments, where the agent must find the optimal strategy assuming the opponent always chooses its best move.
  - Includes Minimax and Alpha-Beta Pruning (an optimization of Minimax).
  
### Classical Search 
#### Problem
##### Maze Problem:
- Definition: Given a standard 2D maze problem, consisting of a grid containing 0 or 1, where 0 means accessible and 1 means an obstacle. The start and goal positions are specified.
- Target: Find the shortest path from the start to the goal, moving only in four directions (up, down, left, right). Obstacles cannot be crossed.
- Evaluation Standard: Each movement costs 1, and the solution must find the shortest possible path.

##### Grid World Problem:
- Definition: Similar to the standard 2D maze problem, but supports a more complex environment, such as:
  - Each state (position) can have rewards or punishments.
  - The step cost can be increased or decreased depending on the rewards or punishments.
- Target: Under the conditions of rewards and punishments, move from the start position to the goal position while achieving the lowest total cost.
- Evaluation Standard: By considering both the rewards and the path size, the goal is to find a path with minimal total cost.

##### Eight Puzzle Problem:
- Definition: Given a 3×3 sliding puzzle that contains numbers from 1 to 8 and a blank space (represented by 0), with the state expressed as a 9-tuple.
- Target: Slide the blank space to exchange with adjacent numbers, and transform the initial state into the goal state, ensuring that the numbers are arranged in the specified order.
- Evaluation Standard: Count the number of slides as the cost, and the objective is to reach the goal state with the minimal number of slides.

#### Algorithm
##### BFS(Breadth-First Search):
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

##### DFS (Depth-First Search):
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
  
##### UCS (Uniform Cost Search):
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
  
##### A* (A Star Search):
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

#### Results
##### Maze Problem

##### Grid World Problem

##### Eight Puzzle Problem
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



    




