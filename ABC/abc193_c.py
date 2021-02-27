N = int(input())
sq = int(N**0.5)
s = set()
for p in range(2, sq + 1):
  x = p*p
  while x <= N:
    s.add(x)
    x *= p

print(N-len(s))