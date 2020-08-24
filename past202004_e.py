N = int(input())

A = list(map(int, input().split()))

L = []
for i in range(1, N+1):
  count = 1

  currentIndex = A[i-1]
  while i != currentIndex:
    currentIndex = A[currentIndex-1]
    count += 1
  
  L.append(count)

print(' '.join(map(str,L)))
