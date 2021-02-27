import numpy as np
N = int(input())

l = []
for i in range(2, N+1):
  l.append(i)

ans = int(np.lcm.reduce(l))+1
print(ans)
for i in range(2, N+1):
  print(ans%i)