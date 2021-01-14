import math
N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    g = math.gcd(a, b)
    for c in range(1, K+1):
      ans += math.gcd(c, g)

print(ans)