N = input()
length = len(N)

mn = float('inf')
for bit in range(1<<length):
  ans = ""
  count = 0
  for i in range(length):
    if bit & (1<<i):
      count += 1
    else:
      ans += N[i]
  if len(ans) >= 1:
    if int(ans) % 3 == 0:
      mn = min(count, mn)
if mn == float('inf'):
  print("-1")
else:  
  print(mn)

