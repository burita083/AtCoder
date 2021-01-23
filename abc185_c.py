L = int(input())

from operator import mul
from functools import reduce
 
 
def cmb(n, r):
	if n < r:
		return 0
	r = min(n - r, r)
	if r == 0:
		return 1
	numer = reduce(mul, range(n, n - r, -1))
	denom = reduce(mul, range(1, r + 1))
	return numer // denom 


d = {}
for i in range(12, 201):
  d[i] = cmb(i-1, 11)
print(d[L])
