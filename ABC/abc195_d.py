import copy

N, M, Q = map(int, input().split())
box = [[] for i in range(10**6+1)]
for i in range(N):
  W, V = map(int, input().split())
  box[W].append(V)

for b in box:
  b.sort()
X = list(map(int, input().split()))
for i in range(Q):
  L, R = map(int, input().split())
  l = range(L, R+1)
  current = copy.deepcopy(box)
  ans = 0
  for i in range(M):
    mx = -1
    if i+1 in l: 
      continue
    for k in reversed(range(X[i]+1)):
      if k == 0: continue
      if len(current[k]) >= 1:
        ans += current[k].pop()
        break
  print(ans)
  



