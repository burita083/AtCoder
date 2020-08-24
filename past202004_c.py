N = int(input())
S = []
for _ in range(N):
  S.append(input())

for i in reversed(range(N)):
  if i == N-1:
    continue

  for k, x in enumerate(S[i]):
    if k+1 >= 2 and k+1 <= 2*N-2:
      if x == "#":
        if S[i+1][k-1] == "X" or S[i+1][k] == "X" or S[i+1][k+1] == "X":
          l = list(S[i])
          l[k] = "X"
          S[i] = "".join(l)

for x in S:
  print(x)
