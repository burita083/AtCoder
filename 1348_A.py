from operator import mul
from functools import reduce
 
 
INF = 1000000007
def cmb(n, r):
	if n < r:
		return 0
	r = min(n - r, r)
	if r == 0:
		return 1
	numer = reduce(mul, range(n, n - r, -1))
	denom = reduce(mul, range(1, r + 1))
	return numer // denom % INF


t = int(input())
for n in range(t):
  print(n)

print(cmb(30, 16))
