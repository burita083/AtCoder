A = list(map(int, input().split()))

ans = 1000
for x in A:
  ans = min(ans, x)


print(ans)