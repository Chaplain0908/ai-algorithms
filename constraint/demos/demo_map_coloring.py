from constraint.algorithms.csp_solver import backtracking_search
from constraint.problems.map_coloring_solver import create_map_coloring_csp
from constraint.visualize.visualize import draw_map_coloring_solution

variables, domain, constraints = create_map_coloring_csp()
solution = backtracking_search(variables, domain, constraints)

print("Map Coloring Solution:")
for var in sorted(solution):
    print(f"{var}: {solution[var]}")

draw_map_coloring_solution(solution)