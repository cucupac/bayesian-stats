import numpy as np
import matplotlib.pyplot as plt


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

burn_in = 1000
samples_after_burn_in = state_array[burn_in:]

# Calculate the Bayes estimator of ρ based on the simulated chain
bayes_estimator_rho = np.mean(samples_after_burn_in)
print(f"Bayes estimator of ρ based on the simulated chain: {bayes_estimator_rho:.5f}")

##########################################
##   Histogram: latter 50,000 samples   ##
##########################################
plt.figure(figsize=(10, 6))
plt.hist(
    samples_after_burn_in,
    bins=50,
    density=True,
    color="skyblue",
    edgecolor="black",
    alpha=0.7,
)
plt.title("Histogram of ρ Values After Burn-in")
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
ax.set_title("Last 1,000 Realizations of ρ")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()


"""
Results:
Bayes estimator of ρ based on the simulated chain: 0.73152
"""
