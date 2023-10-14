import numpy as np


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
        rate_lambda = 1.0 / (mu_samples[i - 1] * sum_t + alpha)  # Inverse of the scale
        lambda_samples[i] = np.random.gamma(shape_lambda, 1.0 / rate_lambda)

        # Sample mu given lambda and data
        shape_mu = n + d
        rate_mu = 1.0 / (lambda_samples[i] * sum_t + beta)  # Inverse of the scale
        mu_samples[i] = np.random.gamma(shape_mu, 1.0 / rate_mu)

    # Discard burn-in samples
    return lambda_samples[burn_in:], mu_samples[burn_in:]


lambda_final_samples, mu_final_samples = gibbs_sampler(21000, 1000)
