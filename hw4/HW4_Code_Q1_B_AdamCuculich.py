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


def proposal_function(rho_prev):
    return np.random.uniform(rho_prev - 0.1, rho_prev + 0.1)


# Initialization
rho_prev = 0.5
rho = 0.6

# Initial state storage
state_array = [rho_prev, rho]

for i in range(50999):
    rho_prime = proposal_function(rho_prev=rho)
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
#               Animation               ##
##########################################
fig, ax = plt.subplots(figsize=(8, 6))
x_values = np.linspace(-6, 6, 400)
y_values = target_function(x_values)
ax.plot(x_values, y_values, label="Target Function")
ax.set_title("Metropolis Sampling on Target Function")
ax.set_xlabel("ρ")
ax.set_ylabel("f(ρ)")
ax.grid(True)

stored_points = []


def update(frame):
    rho = state_array[frame]
    target_function_value = target_function(rho)
    stored_points.append((rho, target_function_value))
    rho_coords, y_coords = zip(*stored_points)

    ax.plot(rho_coords, y_coords, "ro", markersize=4)


ani = animation.FuncAnimation(
    fig, update, frames=len(state_array), repeat=False, interval=1
)

plt.show()
