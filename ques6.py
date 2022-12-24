m=int(input())
alpha=float(input())
from scipy.stats import poisson
import matplotlib.pyplot as plt

rv = poisson.rvs(alpha, size = m)

bin_edges = np.arange(rv.min()-0.5, rv.max()+1.5, 1)
plt.hist(rv, bins = bin_edges, rwidth = 0.8)
plt.xticks(np.arange(rv.min(), rv.max()+1, 1))
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()