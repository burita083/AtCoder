N, M, Q = map(int, input().split())

d = {}
for x in range(N):
  d[x+1] = N

l = [[] for i in range(N)]

for x in range(Q):
  S = list(map(int, input().split()))
  ans = 0
  if S[0] == 1:
    if len(l[S[1] - 1]) == 0:
      print(0)
    else:
      for x in l[S[1]-1]:
        ans += d[x]
      print(ans)
  else:
    d[S[2]] -= 1
    l[S[1]-1].append(S[2])