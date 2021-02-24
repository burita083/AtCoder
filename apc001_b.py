N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sum(A)
b = sum(B)


tempA = a
tempB = b
for i in range(10):
  tempA += 2
  tempB += 1
  if tempA == tempB:
    print(tempA-a, tempB-b)
