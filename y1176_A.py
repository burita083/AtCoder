A = int(input())

mn = float('inf')
for i in range(2, 10000):
  for j in range(1,61):
    s = i**j
    if s >= A:
      mn = min(mn, i*j)

print(mn)