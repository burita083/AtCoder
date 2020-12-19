N = int(input())

A = list(map(int, input().split()))

cums = [0]
A = sorted(A)
for a in A:
    cums.append(cums[-1] + a)
 
ans = 0
for i in range(N-1):
    ans += A[i] - (cums[-1] - cums[i+1])
print(ans)