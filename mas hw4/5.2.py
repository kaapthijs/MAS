# Import numpy for array operations and scipy for correlation and p-value
import numpy as np
from scipy.stats import pearsonr

# Define the number of experiments, the observed correlation, and the significance level
n = 10
robs = 0.3
alpha = 0.05

# Assume that there is no correlation between A and S
# Generate random samples of A and S from a normal distribution with mean 0 and standard deviation 1
A = np.random.normal(0, 1, n)
S = np.random.normal(0, 1, n)

# Compute the correlation coefficient and the p-value for the observed data
r, p = pearsonr(A, S)
print(f"The correlation coefficient for the observed data is {r:.2f} and the p-value is {p:.2f}")

# Define a function to simulate samples under the null hypothesis of no correlation
def simulate_null(n):
  # Generate random samples of A and S from a normal distribution with mean 0 and standard deviation 1
  A = np.random.normal(0, 1, n)
  S = np.random.normal(0, 1, n)
  # Compute the correlation coefficient and return it
  r, _ = pearsonr(A, S)
  return r

# Define the number of simulations to perform
nsim = 1000

# Initialize an empty list to store the simulated correlation coefficients
rsim = []

# Loop over the number of simulations
for i in range(nsim):
  # Simulate a sample under the null hypothesis and append the correlation coefficient to the list
  rsim.append(simulate_null(n))

# Convert the list to a numpy array
rsim = np.array(rsim)

# Compute the proportion of simulated correlation coefficients that are greater than or equal to the observed correlation
prop = np.sum(rsim >= robs) / nsim

# Print the proportion
print(f"The proportion of simulated correlation coefficients that are greater than or equal to the observed correlation is {prop:.2f}")

# Compare the proportion to the significance level and draw a conclusion
if prop < alpha:
  print(f"The observed correlation is significant at the {alpha} level")
else:
  print(f"The observed correlation is not significant at the {alpha} level")
