N = int(input())
ans = [0] * (N + 1)
for i in range (1, 101):
  for j in range(1, 101):
    for k in range(1, 101):
      n = i*i+j*j+k*k+i*j+j*k+k*i
      if n <= N:
        ans[n] += 1

print(*ans[1:], sep='\n')

