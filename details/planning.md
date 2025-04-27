# Planning
In this part, we mainly focus on Classical Planning algorithms.

These algorithms aim to find a sequence of actions that transform an initial state into a goal state, based on given preconditions and effects of actions.

The classic model used here is STRIPS (Stanford Research Institute Problem Solver).

# Planning Subsections
- [Problems](#problems)
  - [STRIPS Model](#strips-model)
- [Algorithm](#algorithm)
  - [Forward Search](#forward-search)
- [Result](#result)
  - [Forward Search Results](#forward-search-results)

# Problems
## STRIPS Model
- Definition: A planning problem where each action is defined by three components:
  - Preconditions: The conditions that must hold before an action can be taken.
  - Add Effects: The facts that will become true after the action is taken.
  - Delete Effects: The facts that will no longer be true after the action is taken.

- Target: Starting from an initial state, apply a sequence of actions to reach a goal state where all goal conditions are satisfied.

- Evaluation: A valid plan must ensure that each action's preconditions are satisfied before being executed, and after applying all actions, the resulting state should satisfy the goal state.

- Required Interfaces:
  - `Action` class:
    - `is_applicable(state)`: Check whether an action can be applied in a given state.
    - `apply(state)`: Apply the action and return the new state.
  - `get_example_planning_problem()`: Return a sample planning problem including:
    - `initial_state`: A set of predicates representing the starting situation.
    - `goal_state`: A set of predicates representing the target.
    - `actions`: A list of available actions.

# Algorithm
## Forward Search
- Propose: A search method that starts from the initial state and applies actions step-by-step to generate new states, continuing until the goal state is satisfied.

- Input & Output:
  - Input:
    - `initial_state`: A set of predicates representing the start.
    - `goal_state`: A set of predicates to be satisfied.
    - `actions`: A list of available `Action` objects.
    - `method`: The search strategy to use ('bfs', 'dfs', or 'astar').
  - Output:
    - A list of action names representing a valid plan from the initial state to the goal state, or `None` if no plan is found.

- Idea:
  - Start from the initial state.
  - Expand possible actions that are applicable.
  - Apply actions to reach new states.
  - Continue expanding states until the goal state is reached.

- Algorithm Step:
```
def forward_search(initial_state, goal_state, actions, method):
    if method == 'bfs':
        return forward_search_bfs(initial_state, goal_state, actions)
    elif method == 'dfs':
        return forward_search_dfs(initial_state, goal_state, actions)
    elif method == 'astar':
        return forward_search_astar(initial_state, goal_state, actions)

def forward_search_bfs(initial_state, goal_state, actions):
    initialize a queue with (initial_state, empty_plan)
    mark initial_state as visited
    while queue is not empty:
        pop (current_state, plan) from queue
        if goal_state is subset of current_state:
            return plan
        for each action in actions:
            if action.is_applicable(current_state):
                next_state = action.apply(current_state)
                if next_state not visited:
                    add (next_state, plan + [action.name]) to queue
                    mark next_state as visited
    return None
```

# Result
## Forward Search Results
Given:
```
Initial State: {"At(R1)"}
Goal State: {"At(R3)"}
Actions:
- Move(R1, R2): Preconditions [At(R1)] -> Add [At(R2)] / Delete [At(R1)]
- Move(R2, R3): Preconditions [At(R2)] -> Add [At(R3)] / Delete [At(R2)]
- Move(R3, R1): Preconditions [At(R3)] -> Add [At(R1)] / Delete [At(R3)]
```

Results:
```
BFS Plan:
['Move(R1,R2)', 'Move(R2,R3)']

DFS Plan:
['Move(R1,R2)', 'Move(R2,R3)']

A* Plan:
['Move(R1,R2)', 'Move(R2,R3)']
```

Visualization Example:
```
Initial State:
['At(R1)']
========================================
Step 1: Apply action -> Move(R1,R2)
  Preconditions: ['At(R1)']
  Effects: +['At(R2)']  -['At(R1)']
  New State: ['At(R2)']
----------------------------------------
Step 2: Apply action -> Move(R2,R3)
  Preconditions: ['At(R2)']
  Effects: +['At(R3)']  -['At(R2)']
  New State: ['At(R3)']
----------------------------------------
Goal Reached!
```

