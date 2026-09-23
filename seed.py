import numpy as np

np.random.seed(42)  # You can replace 42 with any integer
print("\n Set seed \n")
print(np.random.rand(10))
print(np.random.rand(10))
print("\n-- \n Set seed \n")
np.random.seed(42)  # You can replace 42 with any integer                      
print(np.random.rand(10))
print("\n-- \n Set seed \n")
np.random.seed(42)  # You can replace 42 with any integer
print(np.random.rand(20))
