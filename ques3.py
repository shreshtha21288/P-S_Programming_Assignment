m=int(input())
p=float(input())
import matplotlib.pyplot as plt
from scipy.stats import uniform
import numpy as np
data_uniform = uniform.rvs(size=m, loc=0, scale=1)
#print(data_uniform)
bernoulli = np.where(data_uniform < p, 1, 0)

bin_edges = np.arange(bernoulli.min()-0.5, bernoulli.max()+1.5, 1)
plt.hist(bernoulli, bins = bin_edges, rwidth = 0.8)
plt.xticks(np.arange(bernoulli.min(), bernoulli.max()+1, 1))
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()