import itertools
N = int(input())
S = input()

d = {}
for i in range(N):
  d[i] = S[i]

l = list(itertools.combinations(d, 3))
ans = 0
for x in l:
  if d[x[0]] == d[x[1]] or d[x[0]] == d[x[2]] or d[x[1]] == d[x[2]]:
    continue

  if (x[1] - x[0] != x[2] - x[1]):
    ans += 1

print(ans)

