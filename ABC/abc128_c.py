N, M = map(int, input().split())

S = []
for i in range(M):
  A = list(map(int, input().split()))
  l = []
  for i in range(A[0]):
    l.append(A[i+1])
  S.append(l)

P = list(map(int, input().split()))

OnOff = []
ans = 0
for bit in range(1<<N):
  l = []
  for s in range(N):
    if bit & (1<<s):
      l.append(True)
    else:
      l.append(False)
  flagCount = 0
  for i, s in enumerate(S):
    count = 0
    for ss in s:
      if l[ss-1]: 
        count += 1
    if count % 2 == P[i]:
      flagCount += 1
  if flagCount == M:
    ans += 1
print(ans)