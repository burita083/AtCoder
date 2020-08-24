import collections
N = int(input())

l = []
for x in range(N):
  s = input()
  l.append(s)

c = collections.Counter(l)

print(len(c))
