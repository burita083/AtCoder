S = input()
T = input()

tl = len(T)

ans = 100000
for i in range(len(S)-tl+1):
  count = 0
  for j in range(tl):
    if S[i+j] != T[j]:
      count += 1
  ans = min(ans, count)

print(ans)