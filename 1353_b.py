t = int(input())

for i in range(t):
  N, K = map(int, input().split())
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))
  A.sort()
  B.sort(reverse=True)
  count = 0
  for i in range(K):
    if A[i] < B[i]:
      A[i] = B[i]
  print(sum(A))