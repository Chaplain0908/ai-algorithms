import  matplotlib.pyplot as plt
import  numpy as np


def draw_path(grid, path, start, goal, title, save, filename=None):
    """
    grid: 2D numpy array (0 = free, 1 = wall)
    path: list of actions (['Down', 'Right', ...])
    start: tuple (x, y)
    goal: tuple (x, y)
    save: whether to save the figure to file
    """

    # path from start to goal
    position = [start]
    cur_pos = start

    for action in path:
        x, y = cur_pos
        if action == "Up":
            x -= 1
        if action == "Down":
            x += 1
        if action == "Left":
            y -= 1
        if action == "Right":
            y += 1
        cur_pos = (x, y)
        position.append(cur_pos)

    # crate canvas
    fig, ax = plt.subplots(figsize=(8,8))
    rows, cols = grid.shape

    # background grid
    for x in range(rows):
        for y in range(cols):

            # left corner if the original point of matplotlib
            draw_x = y
            draw_y = rows-x-1

            if grid[x, y] == 1: # if there is a wall
                ax.add_patch(plt.Rectangle((draw_x, draw_y), 1, 1, color='black'))
            else:
                ax.add_patch(plt.Rectangle((draw_x, draw_y), 1, 1, edgecolor='gray', facecolor='white'))

    # draw the path line
    for i in range(len(position)-1):
        x1, y1 = position[i]
        x2, y2 = position[i+1]
        draw_x1 = y1+0.5
        draw_y1 = rows-x1-0.5
        draw_x2 = y2+0.5
        draw_y2 = rows-x2-0.5
        ax.plot([draw_x1, draw_x2], [draw_y1, draw_y2], color='blue', linewidth=2)

    # have a green point in start
    sx, sy = start
    draw_sx = sy
    draw_sy = rows-sx-1
    ax.add_patch(plt.Rectangle((draw_sx, draw_sy), 1, 1, facecolor='green'))

    # have a red point in goal
    gx, gy = goal
    draw_gx = gy
    draw_gy = rows-gy-1
    ax.add_patch(plt.Rectangle((draw_gx, draw_gy), 1, 1, facecolor='red'))

    # title
    ax.set_title(title)

    # close the axis scale marks
    ax.set_xticks([])
    ax.set_yticks([])

    # display full coverage
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)

    # save graph
    if save and filename:
        plt.savefig(filename)

    plt.show()



