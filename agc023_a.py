N = int(input())
A = list(map(int, input().split()))

cums = [0]
for a in A:
  cums.append(cums[-1] + a)

ans = 0
print(cums)
for i in range(1, N+1):
  mx = 0
  for j in range(0, N+1-i):
    if cums[j+i]-cums[j] == 0:
      print(cums[j+i], cums[j], j+i, j, i)
      ans += 1
print(ans)