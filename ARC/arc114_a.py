N = int(input())
X = list(map(int, input().split()))

l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
length = len(l)
mn = float('inf')
from math import gcd
for bit in range(1<<length):
  ans = 1
  flag = False
  for i in range(length):
    if bit & (1<<i):
      ans *= l[i]
  if all(gcd(ans, x) != 1 for x in X):
    mn = min(ans, mn)
print(mn)

