K, S = map(int, input().split())
ans = 0

for x in range(K+1):
  for y in range(K+1):
    z = S-x-y
    if z < 0 or z > K:
      continue
    if x + y + z == S:
      ans +=1
print(ans)
