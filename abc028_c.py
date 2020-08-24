import itertools
a, b, c, d, e = map(int, input().split())
 
list = []
for i in itertools.permutations([a, b, c, d, e], r=3):
  print(i)