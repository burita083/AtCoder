from operator import mul
from functools import reduce

mod = 7+10**9
def ncr(n,c,mod):
  x = 1
  y = 1
  for i in range(n-c+1,n+1):
    x = x*i%mod
  for j in range(1,c+1):
    y = y*j%mod
  return (x * pow(y, mod-2, mod)) % mod


N, K = map(int, input().split())

for i in range(1, K + 1):
	print(ncr(K - 1, i - 1, mod) * ncr(N - K + 1, i, mod) % mod)