N = int(input())

m = [0] * (N+1)
for i in range(1, N+1):
  temp = i
  for k in range(temp, N+1, i):
    m[k] += 1
ans = 0
for n in range(1, N+1):
  ans += n*m[n]
print(ans)