N = int(input())

A = list(map(int, input().split()))

count = 0
for i, a in enumerate(A):
  if (i + 1) % 2 != 0 and a % 2 != 0:
    count += 1

print(count)