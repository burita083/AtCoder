X, K, D = map(int, input().split())

ans = 1000000000000007
prev = 1000000000000007
l = 1
r = K
if X < 0:
  while r-l > 1:
    middle = (r+l) // 2
    if X + middle*D == 0:
      print(0)
      exit()
    else:
      if X + middle*D > 0:
        r = middle
      else:
        l = middle
      mn = abs(X + middle * D)
      ans = abs(min(mn, ans))
else:
  while r-l > 1:
    middle = (r+l) // 2
    if X - middle*D == 0:
      print(0)
      exit()
    else:
      if X - middle*D > 0:
        l = middle
      else:
        r = middle
      mn = abs(X - middle * D)
      ans = abs(min(mn, ans))


print(ans)
