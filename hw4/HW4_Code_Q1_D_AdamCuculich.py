import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


##########################################
##    Metropolis-Hastings Algorithm     ##
##########################################
def target_function(rho):
    constant_term = (1 / (2 * np.pi * np.sqrt(1 - rho**2))) ** 100
    exponent_term = np.exp(-(221.8903 - 169.0494 * rho) / (2 * (1 - rho**2)))
    return constant_term * exponent_term


def uniform_generator():
    return np.random.uniform(0, 1)


def proposal_function():
    return np.random.uniform(-1, 1)


# Initialization
rho_prev = 0.5
rho = 0.6

# Initial state storage
state_array = [rho_prev, rho]

for i in range(50999):
    rho_prime = proposal_function()
    rho_value = target_function(rho=rho)
    rho_prime_value = target_function(rho=rho_prime)
    alpha = min(1, rho_prime_value / rho_value)
    random_uniform = uniform_generator()

    # move criteria
    if alpha > random_uniform:
        rho_prev = rho
        rho = rho_prime

    state_array.append(rho)

##########################################
##   Histogram: latter 50,000 samples   ##
##########################################
burn_in = 1000
samples_after_burn_in = state_array[burn_in:]

# Plotting
plt.figure(figsize=(10, 6))
plt.hist(
    samples_after_burn_in,
    bins=50,
    density=True,
    color="skyblue",
    edgecolor="black",
    alpha=0.7,
)
plt.title("Histogram of ρ values after Burn-in")
plt.xlabel("ρ")
plt.ylabel("Density")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

##########################################
## Trace Plot: last 1,000 realizations  ##
##########################################
last_1000_realizations = samples_after_burn_in[-1000:]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(range(1000), last_1000_realizations, color="lightblue", linewidth=0.5)
ax.set_ylabel("ρ")
ax.set_xlabel("Iteration")
ax.set_title("Last 1000 Realizations of ρ")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

##########################################
#               Animation               ##
##########################################
fig, ax = plt.subplots(figsize=(8, 6))
rho_values = np.linspace(-6, 6, 400)
target_function_values = target_function(rho_values)
ax.plot(rho_values, target_function_values, label="Target Function")
ax.set_title("Metropolis Sampling on Target Function")
ax.set_xlabel("ρ")
ax.set_ylabel("f(ρ)")
ax.grid(True)

stored_points = []


def update(frame):
    rho = state_array[frame]
    target_function_value = target_function(rho)
    stored_points.append((rho, target_function_value))
    rho_coords, target_function_value_coords = zip(*stored_points)

    ax.plot(rho_coords, target_function_value_coords, "ro", markersize=4)


ani = animation.FuncAnimation(
    fig, update, frames=len(state_array), repeat=False, interval=1
)

plt.show()


"""
Results:
The trace plot is far less dense: the range of the uniform distribution is much larger,
so there are many values that do not make it past the acceptance criteria.

As manifest in the animation, it's clear that an independence proposal is less efficient in
its discovery time.
"""
