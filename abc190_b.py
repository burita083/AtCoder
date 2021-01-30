N, S, D = map(int, input().split())

flag = False
for n in range(N):
  X, Y = map(int, input().split())
  if X >= S or Y <= D: continue
  if X < S or Y > D: flag = True

if flag:
  print("Yes")
else:
  print("No")