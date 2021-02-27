import itertools
N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))


l = []
for i in range(N):
  l.append(i+1)
a = 0
b = 0
for index, ptn in enumerate(list(itertools.permutations(l, N))):
  temp = []
  for PTN in ptn:
    temp.append(PTN)
  if temp == P:
    a = index+1

  if temp == Q:
    b = index+1
print(abs(a-b))
