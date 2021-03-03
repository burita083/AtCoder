N, K = map(int, input().split())

S = []
for _ in range(N):
   s = int(input())
   S.append(s)

ans = 1
r = 0
mx = -1
for l in range(N):
  if S[l] == 0: 
    mx = N 
    break

  while r < N and S[r] * ans <= K:
    ans *= S[r]
    r += 1
  mx = max(r-l, mx)
  if r == l: 
    r += 1
  else:
    ans //= S[l]
print(mx)
  
