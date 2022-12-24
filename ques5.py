m = int(input())
n = int(input())
p = float(input())
import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np

binomial = np.empty(m, dtype=int)

for i in range(m):
  data_uniform = uniform.rvs(size=n, loc=0, scale=1)  # 0.5 0.4 ...
  bernoulli = np.where(data_uniform < p, 1, 0)  # 0 1 1 0 1
  binomial[i] = np.sum(bernoulli) # 3
  
bin_edges = np.arange(binomial.min()-0.5, binomial.max()+1.5, 1)
plt.hist(binomial, bins = bin_edges, rwidth = 0.8)
plt.xticks(np.arange(binomial.min(), binomial.max()+1, 1))
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()