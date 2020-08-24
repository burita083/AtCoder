mod = 7+10**9
def ncr(n,c,mod):
  x = 1
  y = 1
  for i in range(n-c+1,n+1):
    x = x*i%mod
  for j in range(1,c+1):
    y = y*j%mod
  return (x * pow(y, mod-2, mod)) % mod

n, a, b = map(int, input().split())
al = pow(2, n, mod) -1
acr = ncr(n, a, mod)
bcr = ncr(n, b, mod)
print( (al-(acr+bcr))%mod )


import itertools
N = int(input())
L = list(map(int, input().split()))
 
"L個の要素から3つ選ぶ"
listarray = itertools.combinations(L,3)
count = 0
 
for items in listarray:
  a = items[0]
  b = items[1]
  c = items[2]
  if a < b + c and b < c + a and c < a + b:
    count +=1
 
print(count)


"abc132_dを参考。こっちのほうが早い。"
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
	return numer // denom % INF
