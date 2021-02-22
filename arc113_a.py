K = int(input())

count = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    if a*b > K:
      continue
    count += K//a//b

print(count)


