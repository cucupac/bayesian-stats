import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Parameters for the posterior gamma distribution
alpha_posterior = 5.5
beta_posterior = 4

# Generate grid values
xx = np.linspace(0.001, 3, 1000000)
pdf = gamma.pdf(xx, a=alpha_posterior, scale=1 / beta_posterior)

# Sort density values and their indices
sorted_indices = np.argsort(pdf)[::-1]

# Calculate the HPD
cum_prob = 0
hpd_indices = []

for idx in sorted_indices:
    hpd_indices.append(idx)
    cum_prob += pdf[idx] * (xx[1] - xx[0])  # Assuming a uniform grid
    if cum_prob > 0.95:
        break

low = xx[min(hpd_indices)]
high = xx[max(hpd_indices)]

# Calculate k(alpha)
k_alpha = min([pdf[i] for i in hpd_indices])

# Plotting
plt.plot(xx, pdf, color="black", label="PDF")
plt.axvline(low, linestyle="dashed", linewidth=1, label="Set boundaries")
plt.axvline(high, linestyle="dashed", linewidth=1)

# Shading the HPD region
plt.fill_between(
    xx,
    pdf,
    where=(low <= xx) & (xx <= high),
    color="lightgrey",
    label="HPD-credible region",
)
# Adding the k(alpha) line
plt.axhline(k_alpha, color="red", linestyle="-", label="k(α)")

plt.legend()
plt.title("95% HPD credible set of the posterior Gamma distribution")
plt.ylim(bottom=0)
plt.xlim(left=0, right=3)
plt.show()

# Print the bounds
print(f"Lower bound of the 95% HPD credible set: {low:.5f}")
print(f"Upper bound of the 95% HPD credible set: {high:.5f}")


"""
Results
Lower bound of the 95% HPD credible set: 0.36915
Upper bound of the 95% HPD credible set: 2.53812
"""
