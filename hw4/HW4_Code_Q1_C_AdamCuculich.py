import numpy as np
import matplotlib.pyplot as plt


##########################################
##    Metropolis-Hastings Algorithm     ##
##########################################
def target_function(x):
    constant_term = (1 / (2 * np.pi * np.sqrt(1 - x**2))) ** 100
    exponent_term = np.exp(-(221.8903 - 169.0494 * x) / (2 * (1 - x**2)))
    return constant_term * exponent_term


def uniform_generator():
    return np.random.uniform(0, 1)


def proposal_function(x_t_minus_1):
    return np.random.uniform(x_t_minus_1 - 0.1, x_t_minus_1 + 0.1)


# Initialization
x_t_minus_1 = 0.5
x_t = 0.6

# Initial state storage
state_array = [x_t_minus_1, x_t]

for i in range(50999):
    x_t_next = proposal_function(x_t_minus_1=x_t)
    x_t_value = target_function(x=x_t)
    x_t_next_value = target_function(x=x_t_next)
    alpha = min(1, x_t_next_value / x_t_value)
    random_uniform = uniform_generator()

    # move criteria
    if alpha > random_uniform:
        x_t_minus_1 = x_t
        x_t = x_t_next

    state_array.append(x_t)


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


"""
Results:
The trace plot is far less dense: the range of the uniform distribution is much larger,
so there are many values that do not make it past the acceptance critera.

As manifest in the animation, it's clear that an independence proposal is less efficient in
its disovery time.
"""
