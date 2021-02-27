import itertools
N, K = map(int, input().split())
l = []
for n in range(1, N+1):
  l.append(n)

count = 0
for c in itertools.product(l, repeat=3):
  a = c[0]
  b = c[1]
  c = c[2]
  A = a+b
  B = b+c
  C = c+a
  if A % K == 0 and B % K == 0 and C % K == 0:
    count += 1

print(count)