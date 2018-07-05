
import matplotlib.pyplot as plt
import numpy as np

nb_samples = 100
X_data = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=nb_samples)

plt.plot(X_data)
plt.show()

def negative_log_likelihood(v):
    l=0.0
    f1 = 1.0 /np.sqrt(2.0 * np.pi * v[1])
    f2 = 2.0 * v[1]
    
    for x in X_data:
        l += np.log(f1 * np.exp(-np.square(x-v[0])/f2))
    return -l

from scipy.optimize import minimize
minimize(fun=negative_log_likelihood, x0=[0.0,1.0])