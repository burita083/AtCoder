t = int(input())

for i in range(t):
  N = int(input())
  A = list(map(int, input().split()))
  st = set(A)
  if len(st) == 1:
    print(0)
  else:
    mn = min(A)
    count = 0
    for a in A:
      if mn != a:
        count += 1
    print(count)

