import copy
l = []
for _ in range(3):
  x = int(input())
  l.append(x)

lc = copy.copy(l)
l = sorted(l, reverse=True)
for x in lc:
  print(l.index(x)+1)
