K = int(input())
S = input()

if len(S) <= K:
  print(S)
else:
  s = S[0:K]
  s += "..."
  print(s)