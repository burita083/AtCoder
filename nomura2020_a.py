H1, M1, H2, M2, K = map(int, input().split())

time1 = 60*H1 + M1
time2 = 60*H2 + M2
time = time2-time1
ans = time - K
if ans < 0:
  print(0)
else:
  print(ans)
