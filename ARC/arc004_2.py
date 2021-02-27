N = int(input())
S = []
for _ in range(N):
  S.append(int(input()))


CS = S[:] 
S.sort()
mx = 0
mn = 0

for x in S:
  mx += x

sum = 0
for s in range(len(S) -1):
  sum += S[s]

if N == 1:
  mx = S[0]
  mn = S[0]
elif N == 2:
  mx = S[0] + S[1]
  mn = S[1] - S[0]
else:
  if sum > S[-1]:
    mn = 0
  else:
    c = 0
    d = 0

    for i, s in enumerate(S):
      if i == len(S) - 1:
        d += s
      else:
        c += s
    mn = d - c


print(mx)
print(mn)