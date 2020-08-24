N, K = map(int, input().split())

A = list(map(int, input().split()))
d = {}

d[1] = A[0]

idx = 1
start = 0
count = 0
while True:
  count += 1
  if K == count:
    print(A[idx-1])
    exit()
  d[idx] = A[idx-1]
  idx = A[idx-1]
  if idx in d:
    start = idx
    break


e = {}
l = []
while True:
  e[start] = A[start-1]
  l.append(e[start])
  start = A[start-1]
  if start in e:
    break


amari = ((K-count-len(l)) % len(l))
if amari != 0:
  print(l[amari-1])
else:
  print(l[-1])

