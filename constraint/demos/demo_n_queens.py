from constraint.algorithms.csp_solver import backtracking_search
from constraint.problems.nqueens_solver import create_nqueens_csp
from constraint.visualize.visualize import draw_nqueens_solution

variables, domain, constraints = create_nqueens_csp(8)
solution = backtracking_search(variables, domain, constraints)

print(solution)
draw_nqueens_solution(solution, 8)

