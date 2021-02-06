from itertools import accumulate
A=[1,4,3,4,6,5]
S = list(accumulate(A))
print(S)
print(S[2] - S[1])

N = int(input())
A = list(map(int, input().split()))

cums = [0]
for a in A:
  cums.append(cums[-1] + a)

ans = []
for i in range(1, N+1):
  mx = 0
  for j in range(0, N+1-i):
    mx = max(cums[j+i]-cums[j], mx)
  ans.append(mx)
print(*ans, sep='\n')