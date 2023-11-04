import numpy as np
import matplotlib.pyplot as plt


def gibbs_sampler_for_theta(num_samples, burn_in, y):
    theta_1_samples = np.zeros(num_samples + burn_in)
    theta_2_samples = np.zeros(num_samples + burn_in)
    v_squared_samples = np.zeros(num_samples + burn_in)

    theta_1_samples[0], theta_2_samples[0], v_squared_samples[0] = 0.1, 0.1, 2

    for i in range(1, num_samples + burn_in):
        v_squared = v_squared_samples[i - 1]

        # Sample theta_1 given y, theta_2, and v^2
        mean_theta_1 = v_squared * (0.5 - theta_2_samples[i - 1]) / (v_squared + 1)
        var_theta_1 = v_squared / (v_squared + 1)
        theta_1_samples[i] = np.random.normal(mean_theta_1, np.sqrt(var_theta_1))

        # Sample theta_2 given y, theta_1, and v^2
        mean_theta_2 = v_squared * (0.5 - theta_1_samples[i]) / (v_squared + 1)
        var_theta_2 = v_squared / (v_squared + 1)
        theta_2_samples[i] = np.random.normal(mean_theta_2, np.sqrt(var_theta_2))

        # Sample v^2 given theta_1 and theta_2
        a = 23
        b = (theta_1_samples[i] ** 2 + theta_2_samples[i] ** 2) / 2 + 10
        v_squared_samples[i] = 1 / np.random.gamma(a, 1 / b)

    return (
        theta_1_samples[burn_in:],
        theta_2_samples[burn_in:],
        v_squared_samples[burn_in:],
    )


y_observed = 0.5  # example observation
(
    theta_1_final_samples,
    theta_2_final_samples,
    v_squared_final_samples,
) = gibbs_sampler_for_theta(21000, 1000, y_observed)

theta_1_mean = np.mean(theta_1_final_samples)
theta_1_2_5_percentile = np.percentile(theta_1_final_samples, 2.5)
theta_1_97_5_percentile = np.percentile(theta_1_final_samples, 97.5)

print(f"θ1 Mean: {theta_1_mean:.4f}")
print(
    f"θ1 95% Credible Interval: ({theta_1_2_5_percentile:.4f}, {theta_1_97_5_percentile:.4f})"
)

theta_2_mean = np.mean(theta_2_final_samples)
theta_2_2_5_percentile = np.percentile(theta_2_final_samples, 2.5)
theta_2_97_5_percentile = np.percentile(theta_2_final_samples, 97.5)

print(f"\nθ2 Mean: {theta_2_mean:.4f}")
print(
    f"θ2 95% Credible Interval: ({theta_2_2_5_percentile:.4f}, {theta_2_97_5_percentile:.4f})"
)

v_squared_mean = np.mean(v_squared_final_samples)
v_squared_2_5_percentile = np.percentile(v_squared_final_samples, 2.5)
v_squared_97_5_percentile = np.percentile(v_squared_final_samples, 97.5)

print(f"\nv^2 Mean: {v_squared_mean:.4f}")
print(
    f"v^2 95% Credible Interval: ({v_squared_2_5_percentile:.4f}, {v_squared_97_5_percentile:.4f})"
)

plt.hist(theta_1_final_samples, bins=50, density=True, alpha=0.75, label="θ1")
plt.title("Histogram of θ1")
plt.xlabel("θ1")
plt.ylabel("Density")
plt.legend()
plt.show()

plt.hist(theta_2_final_samples, bins=50, density=True, alpha=0.75, label="θ2")
plt.title("Histogram of θ2")
plt.xlabel("θ2")
plt.ylabel("Density")
plt.legend()
plt.show()

plt.hist(v_squared_final_samples, bins=50, density=True, alpha=0.75, label="v^2")
plt.title("Histogram of v^2")
plt.xlabel("v^2")
plt.ylabel("Density")
plt.legend()
plt.show()


"""
Results:
θ1 Mean: 0.1270
θ1 95% Credible Interval: (-1.0486, 1.3171)

θ2 Mean: 0.1129
θ2 95% Credible Interval: (-1.0719, 1.3171)

v^2 Mean: 0.4717
v^2 95% Credible Interval: (0.3097, 0.7184)
"""
