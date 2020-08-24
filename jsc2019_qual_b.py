N, K = map(int, input().split())

A = list(map(int, input().split()))

mod = 1000000007
count = 0
for i in range(len(A)-1):
  for j in range(i, len(A)):
    if A[i] > A[j]:
      count += 1

A.sort(reverse=True)
count_ = 0
for i in range(len(A)-1):
  for j in range(i, len(A)):
    if A[i] > A[j]:
      count_ += 1

sum1 = count * K

K = K-1
sum = K*(K+1)//2

sum2 = count_ * sum
print((sum1 + sum2)%mod)
