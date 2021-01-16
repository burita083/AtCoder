N = int(input())

A = list(map(int, input().split()))

cums = [0]
aa = 0
for a in A:
  aa += a
  cums.append(aa)

ans = []
for i in range(1, N+1):
  mx = 0
  for j in range(0, N-i+1):
    mx = max(cums[j+i]-cums[j], mx)
  ans.append(mx)
print(*ans, sep='\n')