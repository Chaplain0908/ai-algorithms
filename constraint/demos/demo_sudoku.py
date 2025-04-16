from constraint.algorithms.csp_solver import backtracking_search
from constraint.problems.sudoku_solvers import create_sudoku_csp
from constraint.visualize import draw_sudoku_solution

grid = [[0 for _ in range(9)] for _ in range(9)]

'''
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]
'''

variables, domain, constraints = create_sudoku_csp(grid)
solution = backtracking_search(variables, domain, constraints)

print(solution)
draw_sudoku_solution(solution)