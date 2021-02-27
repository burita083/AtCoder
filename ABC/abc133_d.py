N = int(input())
A = list(map(int, input().split()))

e = sum(A[::2])
o = sum(A[1::2])
ans = [e-o]
for a in A:
  ans.append(2*(a-ans[-1]//2))

ans.pop()
print(*ans)
