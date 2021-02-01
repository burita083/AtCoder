n = int(input())

A = list(map(int, input().split()))

sm = 0
for i in range(1, n):
  sm += A[i]-A[i-1]
print(sm/(n-1))
