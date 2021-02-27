import math
N = int(input())

X = list(map(int, input().split()))

ansA = 0
ansB = 0
ansC = 0
for x in X:
  temp = abs(x)
  ansA += abs(x)
  ansB += (temp * temp)
  ansC = max(ansC, temp)

print(ansA)
print(math.sqrt(ansB))
print(ansC)