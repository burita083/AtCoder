S, L, R = map(int, input().split())

if S >= L and S <= R:
  print(S)
  exit()

if S <= L:
  print(L)
  exit()

if S >= R:
  print(R)
  exit()

A = list(map(int, input().split()))