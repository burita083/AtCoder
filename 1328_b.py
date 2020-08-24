import itertools
t = int(input())
for _ in range(t):
  N, K = map(int, input().split())
  s = ["a"] * (N-2)
  s += ["b"] * 2
  p = itertools.permutations(s, N)
  d = []
  count = 0
  for x in p:
    if x not in d: 
        count += 1
        d.append(x) 
        if count == K:
          print(''.join(x)) 
