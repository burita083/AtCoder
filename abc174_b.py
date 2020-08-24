import math
N, D = map(int, input().split())

count = 0
for i in range(N):
  X, Y = map(int, input().split())
  if math.sqrt(X*X+Y*Y) <= D:
    count += 1

print(count)
