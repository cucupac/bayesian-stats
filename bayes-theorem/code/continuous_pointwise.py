import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# Re-defining the normal distribution function
def normal_dist(x, mean, std):
    return norm.pdf(x, mean, std)


# Parameters for the two normal distributions with increased standard deviations
mean1, std1 = 0, 1  # Likelihood with a wider spread
mean2, std2 = 0.5, 1.2  # Prior with a slightly wider spread

# Range of theta values
theta_values = np.linspace(-5, 5, 1000)

# Calculate the new distributions
dist1 = normal_dist(theta_values, mean1, std1)
dist2 = normal_dist(theta_values, mean2, std2)

# Pointwise multiplication of the two distributions
product_dist = dist1 * dist2

# Plotting with the new parameters and color fill
plt.figure(figsize=(12, 6))

# Adjusted alpha values for the fills based on the visual provided
plt.fill_between(
    theta_values,
    dist1,
    color="red",
    alpha=0.1,
    label="f(x|θ) (Likelihood)",
    edgecolor="red",
    linewidth=2,
)
plt.fill_between(
    theta_values,
    dist2,
    color="blue",
    alpha=0.1,
    label="π(θ) (Prior)",
    edgecolor="blue",
    linewidth=2,
)
plt.fill_between(
    theta_values,
    product_dist,
    color="purple",
    alpha=0.6,
    label="Unnormalized Posterior (Product Distribution)",
    edgecolor="purple",
    linewidth=2,
)

# Drawing the solid lines for the distributions
plt.plot(theta_values, dist1, color="red")
plt.plot(theta_values, dist2, color="blue")
plt.plot(theta_values, product_dist, color="purple")

plt.xlabel("θ")
plt.ylabel("Density")
plt.title("Pointwise Multiplication of Two Normal Distributions")
plt.legend()
plt.grid(True)
plt.show()
