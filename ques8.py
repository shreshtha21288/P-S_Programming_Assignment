from matplotlib import pyplot as mp
from numpy import random 

m=int(input())
lda=float(input())

# print(data)
data = random.exponential(1.0/lda, size=m)
mp.hist(data, bins = 100) 
mp.show()