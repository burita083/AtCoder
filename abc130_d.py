N, K = map(int, input().split())

A = list(map(int, input().split()))

count = 0
left = 0
right = 0
sum = A[0]

while right < N:
  if sum >= K:
    count += N-right
    left += 1
    sum -= A[left-1]
    
    if right < left:
      right += 1
      sum += A[right-1]
  else:
    right += 1
    sum += A[right-1]

print(count)