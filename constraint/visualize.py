def draw_nqueens_solution(solution, n=8):
    board = [['.' for _ in range(n)] for _ in range(n)]
    for var, (x, y) in solution.items():
        board[x][y] = 'Q'

    for row in board:
        print(row)

def draw_sudoku_solution(solution):
    grid = [[0 for _ in range(9)] for _ in range(9)]
    for (x, y), val in solution.items():
        grid[x][y] = val

    print("\nSolved Sudoku:\n")
    for i, row in enumerate(grid):
        row_str = ''
        for j, val in enumerate(row):
            row_str += f"{val} " if val != 0 else '. '
            if (j + 1) % 3 == 0 and j < 8:
                row_str += '| '
        print(row_str)
        if (i + 1) % 3 == 0 and i < 8:
            print("-" * 21)

def draw_map_coloring_solution(solution):
    print("\nMap Coloring Visualization:\n")

    print(f"        [{solution['NT']:^6}]")
    print(f"       NT")
    print(f"[{solution['WA']:^6}]   [{solution['SA']:^6}]   [{solution['Q']:^6}]")
    print(f" WA        SA        Q")
    print(f"       [{solution['NSW']:^6}]")
    print(f"      NSW")
    print(f"       [{solution['V']:^6}]")
    print(f"        V")
    print(f"       [{solution['T']:^6}]")
    print(f"        T\n")