N, K = map(int, input().split())
A = list(map(int, input().split()))
cums = [0]
c = 0
for a in A:
    c += a
    cums.append(c)
ans = 0
print(cums)
from bisect import bisect_left
for i in range(N):
    j = bisect_left(cums, cums[i]+K)
    print(j)
    ans += N+1-j
print(ans)