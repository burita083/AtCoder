from operator import itemgetter
import collections
N = int(input())

X = list(map(int, input().split()))
d = {} 
for x in X:
  if x in d:
    d[x] += 1
  else:
    d[x] = 1
    
keys = sorted(d.keys(), reverse = True)

for x in X:
  idx = N//2
  d[x] -= 1
  for k in keys:
    idx -= d[k]
    if idx <= 0:
      print(k)
      break
  d[x] += 1