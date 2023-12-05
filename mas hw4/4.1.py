# Import numpy library for numerical computations
import numpy as np

# Set the random seed for reproducibility
np.random.seed(2023)

# Generate 10,000 samples from the standard normal distribution
samples = np.random.normal(0, 1, 10000)

# Calculate the value of cos^2(X) for each sample
values = np.cos(samples)**2

# Calculate the sample mean and standard error of cos^2(X)
sample_mean = np.mean(values)
sample_error = np.std(values) / np.sqrt(len(values))

# Display the results
print(f"The sample mean of cos^2(X) is {sample_mean:.4f}")
print(f"The standard error of the mean is {sample_error:.4f}")