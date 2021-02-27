import itertools
A = list(map(int, input().split()))
 
s = set()
count = 0
for ptn in itertools.combinations(A, 3):
  s.add(sum(ptn))
l = list(s)
l.sort()
print(l[-3])

 