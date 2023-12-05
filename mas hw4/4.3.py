# Import libraries
import numpy as np
from scipy.stats import norm

# Define parameters of normal distributions
mu1 = 0 # mean of f
sigma1 = 1 # standard deviation of f
mu2 = 1 # mean of g
sigma2 = 2 # standard deviation of g

# Define sample size
N = 10000

# Generate samples from f and g
f_samples = np.random.normal(mu1, sigma1, N)
g_samples = np.random.normal(mu2, sigma2, N)

# Evaluate the logarithm of the ratio of the densities at each sample point using the normal PDF
log_ratio = np.log(norm.pdf(f_samples, mu1, sigma1) / norm.pdf(f_samples, mu2, sigma2))

# Compute the average of the logarithm of the ratio
mc_kl = np.mean(log_ratio)

# Print the Monte Carlo estimate of the KL divergence
print("The Monte Carlo estimate of the KL divergence from f to g is:", mc_kl)