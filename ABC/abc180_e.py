import operator
N = int(input())

a = []
first = (1, 1, 1)
count = 0
for _ in range(0, N):
  X, Y, Z = map(int, input().split())
  a.append(
    (X, Y, Z)
  )
  if count == 0:
    first = (X, Y, Z)
    count += 1


A = sorted(a, key=operator.itemgetter(0), reverse=True)
B = sorted(a, key=operator.itemgetter(1), reverse=True)
C = sorted(a, key=operator.itemgetter(2), reverse=True)

f = first
cost = 0
for x in A:
  if x[0] == first[0] and x[1] == first[1] and x[2] == first[2]:
  else:
    cost += abs(x[0]-f[0])
    cost += abs(x[1]-f[1])
    cost += max(0, x[2]-f[2])
  f[0] = x[0]
  f[1] = x[1]
  f[2] = x[2]

