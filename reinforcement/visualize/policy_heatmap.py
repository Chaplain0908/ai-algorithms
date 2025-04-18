import matplotlib.pyplot as plt
import numpy as np

arrow_map = {
    'Up': (0, -0.3),
    'Down': (0, 0.3),
    'Left': (-0.3, 0),
    'Right': (0.3, 0)
}

def plot_policy_and_values(grid, policy, state_values, title="Policy & State Values"):
    rows, cols = len(grid), len(grid[0])
    data = np.zeros((rows, cols))
    arrows = np.full((rows, cols), '', dtype=object)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                data[i][j] = np.nan
                continue
            pos = (i, j)
            data[i][j] = state_values.get(pos, 0.0)
            arrows[i][j] = policy.get(pos, '')

    fig, ax = plt.subplots()
    im = ax.imshow(data, cmap='coolwarm', interpolation='nearest')
    plt.title(title)

    # Draw arrows
    for i in range(rows):
        for j in range(cols):
            action = arrows[i][j]
            if action in arrow_map:
                dx, dy = arrow_map[action]
                ax.arrow(j, i, dx, dy, head_width=0.1, head_length=0.1, fc='k', ec='k')
            elif grid[i][j] == 1:
                ax.text(j, i, 'X', ha='center', va='center', color='black')

    # Show values
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != 1:
                val = state_values.get((i, j), 0.0)
                ax.text(j, i + 0.3, f"{val:.2f}", ha='center', va='center', color='black', fontsize=7)

    plt.colorbar(im)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    plt.show()
