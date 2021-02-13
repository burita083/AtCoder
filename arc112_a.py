T = int(input())
for t in range(T):
  L, R = map(int, input().split())
  count = 0
  for B in range(L, R+1):
    if not L <= R-B <= R: 
      continue
    count += (R-B) - L + 1
  print(count)
