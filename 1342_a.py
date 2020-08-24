t = int(input())

for _ in range(t):
  ansA = 0
  ansB = 0
  x, y = map(int, input().split())
  a, b = map(int, input().split())
  "bのほうがいい"
  if a <= b:
    if 2*a <= b:
      print(a*(x+y))
      continue
    else:
      mn = min(x, y)
      mx = max(x, y)
      ansB += mn
      mx -= mn
      ansA += mx
      print(a*ansA+b*ansB)
      continue
  else:
    mn = min(x, y)
    mx = max(x, y)
    ansB += mn
    mx -= mn
    ansA += mx
    print(a*ansA+b*ansB)
    continue

