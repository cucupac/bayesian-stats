import numpy as np
import matplotlib.pyplot as plt


def gibbs_sampler(num_samples, burn_in):
    # Initialize parameters and hyperparameters
    n = 20
    c, d, alpha, beta = 3, 1, 100, 5
    sum_t = 522
    lambda_samples = np.zeros(num_samples + burn_in)
    mu_samples = np.zeros(num_samples + burn_in)
    product_samples = np.zeros(num_samples + burn_in)
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

        # Save the product for this iteration
        product_samples[i] = lambda_samples[i] * mu_samples[i]

    # Discard burn-in samples
    return lambda_samples[burn_in:], mu_samples[burn_in:], product_samples[burn_in:]


lambda_final_samples, mu_final_samples, product_samples = gibbs_sampler(21000, 1000)

# Average the products for the Bayesian estimate
bayes_estimator = np.mean(product_samples)

print("Bayes Estimator:", bayes_estimator)


"""
Results:
Bayes Estimator of Product: 0.03368101273630085
"""
