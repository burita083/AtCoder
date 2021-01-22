from itertools import accumulate
N, C = map(int, input().split())

d = {}
for _ in range(N):
  a, b, c = map(int, input().split())
  d.setdefault(a, 0)
  d[a] += c
  d.setdefault(b+1, 0)
  d[b+1] -= c
sd = sorted(d)
for i in range(1, len(sd)):
  d[sd[i]] += d[sd[i-1]]
for k in d:
  if d[k] > C:
    d[k] = C

ans = 0

for i in range(len(sd)-1):
  ans += d[sd[i]]*(sd[i+1]-sd[i])
print(ans)
