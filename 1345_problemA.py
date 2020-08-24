t = int(input())

for x in range(t):
  n, m = map(int, input().split())
  if n >= 3:
    if m >= 2:
      print("NO")
      continue
    else:
      print("YES")
      continue

  if m >= 3:
    if n >= 2:
      print("NO")
      continue
    else:
      print("YES")
      continue

  if n <= 2 and m <= 2:
    print("YES")
    continue