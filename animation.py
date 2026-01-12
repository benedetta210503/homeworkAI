import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

def draw_board(ax, state, n):
    ax.clear()
    for i in range(n):
        for j in range(n):
            color = 'white' if (i+j)%2==0 else 'black'
            rect = patches.Rectangle((j, n-1-i), 1, 1, facecolor=color)
            ax.add_patch(rect)

    for row, col in enumerate(state):
        if row < n:
            circle = patches.Circle((col + 0.5, n-1-row + 0.5), 0.3, facecolor='red')
            ax.add_patch(circle)

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect('equal')

def animate_solution(solution_path, n, interval=600):
    fig, ax = plt.subplots(figsize=(6,6))

    def update(frame):
        state = solution_path[frame]
        draw_board(ax, state, n)
        ax.set_title(f"Step {frame+1}/{len(solution_path)}")

    ani = FuncAnimation(fig, update, frames=len(solution_path), interval=interval, repeat=False)
    plt.show()
