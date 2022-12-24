m=int(input())
p=float(input())
geometric = np.empty(m, dtype = int)
for i in range(m):
  x = 0
  val = 0
  while x == 0:
    val = val+1
    data_uniform = uniform.rvs(size=1, loc=0, scale=1)
    # print(data_uniform[0])
    if data_uniform[0] < p:
      x = 1
  geometric[i] = val

bin_edges = np.arange(geometric.min()-0.5, geometric.max()+1.5, 1)
plt.hist(geometric, bins = bin_edges, rwidth = 0.8)
plt.xticks(np.arange(geometric.min(), geometric.max()+1, 1))
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()