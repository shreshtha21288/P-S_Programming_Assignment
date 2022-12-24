import numpy as np
import matplotlib.pyplot as plt

#Generate 100 samples that are uniformly distributed over (0,1).
data = np.random.uniform(0,1,100)

count, bins, ignored = plt.hist(data, 10)

pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins[1:], cdf, label="CDF")
#plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.legend()
plt.show()