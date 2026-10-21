import numpy as np

# Number of samples
N = 100000

# Generate random samples in [0, 1]
x = np.random.rand(N)

# Compute e^x for each sample
y = np.exp(x)

# Monte Carlo estimate of the integral
monte_carlo_estimate = np.mean(y)

# Exact value of the integral ∫₀¹ e^x dx = e - 1
exact_value = np.exp(1) - 1

# Error analysis
absolute_error = abs(monte_carlo_estimate - exact_value)

# Display results
print(f"Monte Carlo estimate: {monte_carlo_estimate:.5f}")
print(f"Exact value= e-1:          {exact_value:.5f}")
print(f"Absolute error:       {absolute_error:.5f} \n --- \n ")

x = np.random.uniform(0, np.pi, 100000)
y = np.sin(x)
estimate = np.pi * np.mean(y)
exact_value = 2
print(f"Monte Carlo estimate ∫₀^π sin(x) dx: {estimate}")
print(f"Exact value:          {exact_value:.5f}")