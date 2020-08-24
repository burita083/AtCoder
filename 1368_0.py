t = int(input())

for i in range(t):
  ans = 0
  count = 0
  a, b, n = map(int, input().split())
  while ans <= n:
    if a >= b:
      b += a
      ans = b
    else:
      a += b
      ans = a
    count += 1
  print(count)