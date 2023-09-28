import numpy as np
from scipy.special import gammaincc  # This is the upper incomplete gamma function
from scipy.optimize import brentq  # A root-finding routine


# Define the equation for L
def equation_L(L):
    return 1 - gammaincc(5.5, 4 * L) - 0.025


# Define the equation for U
def equation_U(U):
    return gammaincc(5.5, 4 * U) - 0.025


# Using the brentq method to find the roots
L = brentq(
    equation_L, 0, 10
)  # The numbers 0 and 10 define the interval in which we search for a root
U = brentq(equation_U, 0, 10)

print("L:", L)
print("U:", U)

"""
Results
L: 0.4769685315295111
U: 2.7400061576274726
"""
