import numpy as np
from scipy.stats import gamma
from scipy.optimize import fmin


# Define the negative of the posterior.
# This is because we're going to use a minimization routine to maximize this function.
def negative_posterior(theta, alpha, beta):
    # Return negative of Gamma PDF. This is because we want to maximize the posterior.
    return -gamma.pdf(theta, a=alpha, scale=1 / beta)


alpha = 5.5
beta = 4

# Start the optimization at some reasonable starting value, like 1
initial_guess = [1]

# Use fmin to minimize the negative posterior
theta_map = fmin(negative_posterior, initial_guess, args=(alpha, beta))

print(f"The MAP estimate of theta is: {theta_map[0]}")


"""
Results:
Optimization terminated successfully.
         Current function value: -0.738473
         Iterations: 12
         Function evaluations: 24
The MAP estimate of theta is: 1.1250000000000002
"""
