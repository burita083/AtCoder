N, M = map(int, input().split())

A = list(map(int, input().split()))

ans = float('inf')
for i in range(N-M+1):
  st = set()
  for j in range(i, i+M):
    st.add(A[j])
  b = range(len(st))
  if set(b) != st:
    c = min(set(b)-st)
    ans = min(c, ans)
  else:
    ans = min(max(st)+1, ans)

print(ans)


ans = 1
r = 0
mx = -1
d = {}
for l in range(N):
  if S[l] == 0: 
    mx = N 
    break
 
  while r <= M and S[r] * ans <= K:
    if A[r] in d:
      d[A[r]] += 1
    else:
      d[A[r]] = 1
    r += 1
  mx = max(r-l, mx)
  if r == l: 
    r += 1
  else:
    ans //= S[l]
print(mx)
