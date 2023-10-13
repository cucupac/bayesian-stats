import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.animation as animation


def target_function(x):
    return 0.5 * norm.pdf(x, -2, 1) + 0.5 * norm.pdf(x, 2, 1)


def uniform_generator():
    return np.random.uniform(0, 1)


def proposal_function(x_t):
    return norm.rvs(loc=x_t, scale=0.4)


# initial state
x_t = 0.6

# initial state storage
state_array = [x_t]

for i in range(5000):
    x_t_next = proposal_function(x_t=x_t)
    x_t_value = target_function(x=x_t)
    x_t_next_value = target_function(x=x_t_next)
    alpha = min(1, x_t_next_value / x_t_value)
    random_uniform = uniform_generator()

    # move criteria
    if alpha > random_uniform:
        # yes, move
        x_t = x_t_next

    state_array.append(x_t)


# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
x_values = np.linspace(-6, 6, 400)
y_values = target_function(x_values)
ax.plot(x_values, y_values, label="Target Function")
ax.set_title("Metropolis Sampling on Target Function")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)

# Initialize a list to store (x,y) pairs of points.
stored_points = []


# Update function for animation
def update(frame):
    x = state_array[frame]
    y = target_function(x)
    stored_points.append((x, y))
    x_coords, y_coords = zip(*stored_points)

    ax.plot(
        x_coords, y_coords, "ro", markersize=4
    )  # Plot all points up to current frame


# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=len(state_array), repeat=False, interval=10
)

plt.show()
