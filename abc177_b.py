S = input()
T = input()

tl = len(T)

ans = -1
for i in range(0, len(S)-tl+1):
  count = 0
  for j in range(0, tl):
    if S[i+j] == T[j]:
      count += 1
  ans = max(ans, count)

print(tl-ans)