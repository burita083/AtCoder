K = int(input())

def gcd(x, y):
  while y != 0:
    (x, y) = (y, x%y)
  return x

ans = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    g = gcd(a, b)
    for c in range(1, K+1):
      ans += gcd(c, g)

print(ans)