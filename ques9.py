m = int(input())
p = float(input())
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import random
import numpy as np

def get_bernoulli(a, m):
  data_bern = bernoulli.rvs(size=m, p=a)
  return data_bern

x = [i for i in range(1,m+1)]
y = []

bern = get_bernoulli(p, m)

bern

for i in range(1,m+1):
  y.append(sum(bern[:i])/i)

y

plt.ylim(0,1)
plt.plot(x,y)
plt.xlabel('Samples')
plt.ylabel('sample mean')
plt.show()

plt.plot(x,bern)
plt.xlabel('Samples')
plt.ylabel('p')
plt.show()