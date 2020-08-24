t = int(input())
for _ in range(t):
  a, b, c, d = map(int, input().split())
  if a <= b:
    print(b)
  else:
    a -= b
    e = c - d
    if e <= 0:
      print(-1)
    else:
      count = 0
      if a % e == 0:
        count += a // e
      else :
        count += a // e
        count += 1
      print(b + count*c)
