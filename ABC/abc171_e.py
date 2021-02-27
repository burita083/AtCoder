N = int(input())

A = list(map(int, input().split()))

x = 0
for a in A:
  x ^= a
  print(x)

ans = []
for a in A:
  print(x^a)
  ans.append(x^a)
print(*ans)