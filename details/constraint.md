# Constrain
In this part, we mainly focus on Constraint Satisfaction algorithms.

These algorithms are designed to solve a type of problem where the goal is to find a valid assignment of variables that satisfies a set of given constraints.

The classic problems for this type of algorithm include map coloring, N-Queens, and Sudoku.

# Constrain Subsections
- [Problems](#problems)
  - [Map Coloring Problem](#map-colouring-problem)
  - [N-Queens Problem](#n-queens-problem)
  - [Sudoku Problem](#sudoku-problem)
- [Algorithm](#algorithm)
  - [CSP_solver](#csp_solver-constraint-satisfaction-problem-solver)
- [Result](#result)
  - [Map Colouring Result](#map-colouring-result)
  - [N-Queens Result](#n-queens-result)
  - [Sudoku Result](#sudoku-result)

# Problems
## Map Colouring Problem
- Definition: Given a map composed of different regions, each region is considered as a variable. 
            The domain for each variable is a set of colors. Adjacent regions must have different colors.
- Target: Assign a color to each region such that no two adjacent regions have the same color.
- Evaluation: A valid solution must ensure that all constraints are satisfied, meaning any two neighboring regions must be colored differently.
- Required Interfaces:
  - create_map_coloring_csp(): Create the CSP model for the map coloring problem. 
    - Return:
      - variables: A list of regions (e.g., 'WA', 'NT', etc.). 
      - domains: A mapping from each region to a list of available colors. 
      - constraints: A list of binary constraints that enforce neighboring regions must have different colors.
  - constraint_fn(value1, value2): Constraint function that checks if two neighboring regions have different colors.

## N-Queens Problem
- Definition: Given an n×n chessboard, place n queens on the board, where each queen is a variable. 
            The domain for each queen is the possible positions in its corresponding row.
- Target: Place all queens on the board so that no two queens attack each other — no two queens can be in the same column, or on the same diagonal.
- Evaluation: A valid solution must satisfy all constraints, meaning that every pair of queens must not threaten each other in columns or diagonals.
- Required Interfaces:
  - create_nqueens_csp(n): Create the CSP model for the N-Queens problem. 
    - Input:
      - n: The number of queens (board size n×n). 
    - Return:
      - variables: A list of queen variables (Q0, Q1, ..., Qn-1). 
      - domains: A mapping from each queen to possible positions in its row. 
      - constraints: A list of binary constraints to ensure no two queens attack each other. 
    - constraint_fn(value1, value2): Constraint function that checks if two queens are not in the same column or diagonal.

## Sudoku Problem
- Definition: Given a standard 9×9 Sudoku grid, each empty cell is treated as a variable. 
            The domain for each variable is the numbers from 1 to 9. The constraints are based on Sudoku rules.
- Target: Fill all the empty cells so that every row, column, and 3×3 subgrid contains all the numbers from 1 to 9 exactly once.
- Evaluation: A valid solution must satisfy that no duplicate numbers appear in any row, column, or 3×3 block.
- Required Interfaces:
  - create_sudoku_csp(grid): Create the CSP model for the Sudoku problem. 
  - Input:
    - grid: The initial Sudoku grid (can contain empty cells). 
  - Return:
    - variables: A list of all cell positions in the 9×9 grid. 
    - domains: A mapping from each cell to possible values (1 to 9). 
    - constraints: A list of binary constraints to ensure Sudoku rules (rows, columns, and 3×3 sub-grids). 
  - constraint_fn(value1, value2): Constraint function that checks if two connected cells have different values.

# Algorithm
## CSP_solver (Constraint Satisfaction Problem Solver)
- Propose: A general search algorithm designed to solve constraint satisfaction problems by trying assignments recursively. 
        It assigns values to variables while checking consistency, and backtracks when a conflict is detected.
- Input & Output:
  - Input:
    - variables: A list of variable names. 
    - domains: A dictionary mapping each variable to its list of possible values. 
    - constraints: A list of binary constraints between variables, where each constraint is a tuple (var1, var2, constraint_fn). 
    - assignment (optional): A dictionary of current variable assignments.
- Output: A complete assignment that satisfies all constraints, or None if no solution exists. 
- Idea:
  - Start with an empty assignment. 
  - Recursively assign a value to an unassigned variable. 
  - After assigning, check whether the partial assignment satisfies all constraints. 
  - If the assignment is valid, continue to assign the next variable. 
  - If a conflict is found, backtrack and try a different value.
- Algorithm Step:
    ```
    def backtracking_search(variables, domains, constraints, assignment):
        if assignment is complete:
            return assignment
        
        var = select an unassigned variable
    
        for each value in domain[var]:
            if value is consistent with assignment:
                assign value to var
                result = backtracking_search(variables, domains, constraints, assignment)
                if result is not None:
                    return result
                remove assignment of var (backtrack)
    
        return None (if no value leads to a solution)
    ```
  
# Result
## Map Colouring Result
Given:
```
# =====（Variables）=====
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# =====（Domains）=====
colors = ['red', 'green', 'blue']
domains = {var: colors.copy() for var in variables} 

# =====（Constraints）=====
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': [] 
}

```
Results:
```
Map Coloring Solution:
NSW: green
NT: green
Q: red
SA: blue
T: red
V: red
WA: red

Map Coloring Visualization:

        [green ]
           NT
[ red  ]   [ blue ]   [ red  ]
  WA         SA         Q
       [green ]
         NSW
       [ red  ]
          V
       [ red  ]
          T
```
## N-Queens Result
```
{'Q0': (0, 0), 'Q1': (1, 4), 'Q2': (2, 7), 'Q3': (3, 5), 'Q4': (4, 2), 'Q5': (5, 6), 'Q6': (6, 1), 'Q7': (7, 3)}
['Q', '.', '.', '.', '.', '.', '.', '.']
['.', '.', '.', '.', 'Q', '.', '.', '.']
['.', '.', '.', '.', '.', '.', '.', 'Q']
['.', '.', '.', '.', '.', 'Q', '.', '.']
['.', '.', 'Q', '.', '.', '.', '.', '.']
['.', '.', '.', '.', '.', '.', 'Q', '.']
['.', 'Q', '.', '.', '.', '.', '.', '.']
['.', '.', '.', 'Q', '.', '.', '.', '.']
```
## Sudoku Result
```
Solved Sudoku:

1 2 3 | 4 5 6 | 7 8 9 
4 5 6 | 7 8 9 | 1 2 3 
7 8 9 | 1 2 3 | 4 5 6 
---------------------
2 1 4 | 3 6 5 | 8 9 7 
3 6 5 | 8 9 7 | 2 1 4
8 9 7 | 2 1 4 | 3 6 5
---------------------
5 3 1 | 6 4 2 | 9 7 8
6 4 2 | 9 7 8 | 5 3 1
9 7 8 | 5 3 1 | 6 4 2
```