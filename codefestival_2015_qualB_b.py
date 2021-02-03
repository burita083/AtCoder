N, M = map(int, input().split())

A = list(map(int, input().split()))

from collections import Counter
C = Counter(A)

count = 0
for k, v in C.items():
  if v > N//2:
    print(k)
    exit()
  
print("?")