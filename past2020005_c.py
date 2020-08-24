A, R, N = map(int, input().split())

count = 2
ans = A
for x in range(1, 1000000001):
  ans = A*(R**x)
  if count < N:
    if ans > 1000000000:
      print("large")
      exit()
    else:
      count +=1
  else:
    if ans > 1000000000:
      print(large)
    else:
      print(ans)
    count +=1