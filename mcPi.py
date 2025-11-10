import numpy as np

np.random.seed(0)
for N in [10,100, 1000, 10000, 100000, 1000000 , 10000000]:
    x = np.random.rand(N, 1) - 1/2
    y = np.random.rand(N, 1) - 1/2
    h = x**2 + y**2
    
    N0 = np.sum(h > 1/4)  # points out of the cercle
    
    estpi = 4 * (N - N0) / N  ## estimation
    
    percentage_err = abs(np.pi - estpi) / np.pi

    print("N=", N, " estimation=", estpi, "% erreur=", percentage_err,"\n")
