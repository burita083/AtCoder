N = int(input())

A = list(map(int, input().split()))

ans = 1
keta = 0
if 0 in A:
  print(0)
  exit()

for x in A:
  ans *= x
  keta += len(str(x))
  if ans > 1000000000000000000:
    print(-1)
    exit()

print(ans)
