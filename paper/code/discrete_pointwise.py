import numpy as np
import matplotlib.pyplot as plt

# Generating sample data for the distributions
data1 = np.random.normal(loc=0, scale=1, size=1000)  # For f(x|θ)
data2_ = np.random.normal(loc=1, scale=1.5, size=1000)  # For  π(θ)

# Creating histograms (discrete distributions) with common bin edges
bins_common = np.linspace(-5, 5, 21)  # 20 bins with a common range
hist1, _ = np.histogram(data1, bins=bins_common, density=True)
hist2_, _ = np.histogram(data2_, bins=bins_common, density=True)

# Calculating the product distribution
product_hist_ = hist1 * hist2_

# Bin centers for plotting
bins_centers_common = (bins_common[:-1] + bins_common[1:]) / 2

# Plotting with adjusted distributions and titles
fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# f(x|θ) with light blue color and black outlines
axs[0].bar(
    bins_centers_common,
    hist1,
    width=bins_common[1] - bins_common[0],
    color="lightblue",
    edgecolor="black",
)
axs[0].set_title("Likelihood, f(x|θ)")
axs[0].set_xlabel("θ")
axs[0].set_ylabel("Density")
axs[0].set_xlim(-5, 5)

#  π(θ) with light blue color and black outlines
axs[1].bar(
    bins_centers_common,
    hist2_,
    width=bins_common[1] - bins_common[0],
    color="lightblue",
    edgecolor="black",
)
axs[1].set_title("Prior, π(θ)")
axs[1].set_xlabel("θ")
axs[1].set_xlim(-5, 5)

# Product distribution with light blue color and black outlines
axs[2].bar(
    bins_centers_common,
    product_hist_,
    width=bins_common[1] - bins_common[0],
    color="lightblue",
    edgecolor="black",
)
axs[2].set_title("Unnormalized Posterior (Product Distribution)")
axs[2].set_xlabel("θ")
axs[2].set_xlim(-5, 5)

plt.tight_layout()
plt.show()
