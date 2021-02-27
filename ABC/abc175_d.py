X, K, D = map(int, input().split())

ans = 1000000000000007
prev = 1000000000000007
if X + D*K < 0:
  print(X+D*K)
  exit()

if X - D*K > 0:
  print(X-D*K)
  exit()


if K % 2 == 0:

  i = K // 2
  for k in range(0, i+1):
    mn = abs(X + k * D * 2)
    if prev < mn:
      break
    prev = mn
    ans = abs(min(mn, ans))

  prev = 1000000000000007
  for k in range(0, i+1):
    mn = abs(X - k * D * 2)
    if prev < mn:
      break
    prev = mn
    ans = abs(min(mn, ans))

else:
  for k in range(1, K+1, 2):
    mn = abs(X + k * D)
    if prev < mn:
      break
    prev = mn
    ans = abs(min(mn, ans))

  prev = 1000000000000007
  for k in range(1, K+1, 2):
    mn = abs(X - k * D)
    if prev < mn:
      break
    prev = mn
    ans = abs(min(mn, ans))

print(ans)
