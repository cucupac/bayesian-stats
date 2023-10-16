import numpy as np
import matplotlib.pyplot as plt


def gibbs_sampler(num_samples, burn_in):
    # Initialize parameters and hyperparameters
    n = 20
    c, d, alpha, beta = 3, 1, 100, 5
    sum_t = 522
    lambda_samples = np.zeros(num_samples + burn_in)
    mu_samples = np.zeros(num_samples + burn_in)
    mu_samples[0] = 0.1  # initial value for mu

    # Gibbs sampling loop
    for i in range(1, num_samples + burn_in):
        # Sample lambda given mu and data
        shape_lambda = n + c
        rate_lambda = mu_samples[i - 1] * sum_t + alpha

        # Stability check
        if rate_lambda > 1e6:
            rate_lambda = 1e6
        elif rate_lambda < 1e-6:
            rate_lambda = 1e-6

        lambda_samples[i] = np.random.gamma(shape_lambda, 1.0 / rate_lambda)

        # Sample mu given lambda and data
        shape_mu = n + d
        rate_mu = lambda_samples[i] * sum_t + beta

        # Stability check
        if rate_mu > 1e6:
            rate_mu = 1e6
        elif rate_mu < 1e-6:
            rate_mu = 1e-6

        mu_samples[i] = np.random.gamma(shape_mu, 1.0 / rate_mu)

    # Discard burn-in samples
    return lambda_samples[burn_in:], mu_samples[burn_in:]


lambda_final_samples, mu_final_samples = gibbs_sampler(21000, 1000)

# Scatterplot of (λ, μ)
plt.scatter(lambda_final_samples, mu_final_samples, alpha=0.5)
plt.xlabel("λ")
plt.ylabel("μ")
plt.title("Scatterplot of (λ, μ)")
plt.show()

# Histogram of λ
plt.hist(lambda_final_samples, bins=50, density=True, alpha=0.75)
plt.title("Histogram of λ")
plt.xlabel("λ")
plt.ylabel("Density")
plt.show()

# Histogram of μ
plt.hist(mu_final_samples, bins=50, density=True, alpha=0.75)
plt.title("Histogram of μ")
plt.xlabel("μ")
plt.ylabel("Density")
plt.show()

# Calculate posterior means and variances
lambda_mean = np.mean(lambda_final_samples)
lambda_variance = np.var(lambda_final_samples)
mu_mean = np.mean(mu_final_samples)
mu_variance = np.var(mu_final_samples)
print(f"λ: Mean = {lambda_mean}, Variance = {lambda_variance}")
print(f"μ: Mean = {mu_mean}, Variance = {mu_variance}")

# Calculate 95% equitailed credible intervals
lambda_credible_interval = np.percentile(lambda_final_samples, [2.5, 97.5])
mu_credible_interval = np.percentile(mu_final_samples, [2.5, 97.5])
print(f"λ: 95% Credible Interval = {lambda_credible_interval}")
print(f"μ: 95% Credible Interval = {mu_credible_interval}")


"""
Results:
λ: Mean = 0.054513434068013684, Variance = 0.0003724312507843258
μ: Mean = 0.6836937608980612, Variance = 0.06585634501123556
λ: 95% Equitailed Credible Set = [0.02532385 0.10026695]
μ: 95% Equitailed Credible Set = [0.30615996 1.30088625]
"""
