from matplotlib import pyplot as mp
import random
import numpy as np

m=int(input())
mu=float(input())
sig=float(input())

nums=[]
for i in range(m): 
    nums.append(random.gauss(mu, sig)) 
# print(nums)       
mp.hist(nums, bins= 100) 
mp.show()