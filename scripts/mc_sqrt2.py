import numpy as np

# Generate random numbers in [0, 2]
x = 2 * np.random.rand(10000)

# Compute y = 1 / sqrt(x)
y = 1 / np.sqrt(x)

# Estimate sqrt(2) as the mean of y
sqrt2_est = np.mean(y)

print(f"Estimated sqrt(2): {sqrt2_est}")