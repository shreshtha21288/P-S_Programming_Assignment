import numpy as np
import matplotlib.pyplot as plt


data = np.random.uniform(75,110,100)
print(sorted(data))
count, bins, ignored = plt.hist(data, 100 )
pdf = count / sum(count)
cdf = np.cumsum(pdf)
plt.plot(bins[1:], cdf, label="CDF")
#plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.legend()
plt.show()